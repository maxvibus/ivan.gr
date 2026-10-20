/* ivan.gr — νύχτα/ημέρα, παράθυρα που ανοίγουν από το πλαίσιο, αναζήτηση */
(function(){
  var root = document.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function norm(s){ return (s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/ς/g,'σ'); }

  /* μετάβαση σελίδων: ο τίτλος που πατήθηκε παίρνει το όνομα του τίτλου της επόμενης σελίδας */
  var lastLink = null;
  document.addEventListener('click', function(e){ var a = e.target.closest && e.target.closest('a[href]'); if(a) lastLink = a; }, true);
  addEventListener('pageswap', function(e){
    if(!e.viewTransition || !lastLink || document.querySelector('.post h1')) return;
    var t = lastLink.querySelector('span') || lastLink;
    t.style.viewTransitionName = 'vt-title';
    e.viewTransition.finished.then(function(){ t.style.viewTransitionName = ''; }, function(){ t.style.viewTransitionName = ''; });
  });

  function ready(fn){ if(document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }
  ready(function(){
    /* νύχτα */
    var btns = document.querySelectorAll('button.night');
    function sync(){ var n = root.dataset.theme === 'night';
      btns.forEach(function(b){ b.setAttribute('aria-pressed', String(n)); b.setAttribute('aria-label', n ? 'Ανάγνωση ημέρας' : 'Νυχτερινή ανάγνωση'); }); }
    sync();
    btns.forEach(function(b){ b.addEventListener('click', function(){
      var n = root.dataset.theme !== 'night';
      if(n) root.dataset.theme = 'night'; else delete root.dataset.theme;
      try{ if(n) localStorage.setItem('ivan-theme','night'); else localStorage.removeItem('ivan-theme'); }catch(e){}
      sync();
    }); });

    /* η γραμμή της ημέρας: ημερομηνία και ώρα του αναγνώστη, και ο ήλιος (ή η σελήνη) πάνω στο τόξο της μέρας */
    var dday = document.querySelector('[data-today]'), clock = document.querySelector('[data-clock]'), arc = document.querySelector('.sunarc');
    if(dday){
      var tick = function(){
        var d = new Date();
        try{ var t = d.toLocaleDateString('el-GR', {weekday:'long', day:'numeric', month:'long', year:'numeric'});
             dday.textContent = t.charAt(0).toUpperCase() + t.slice(1).replace(',', ''); }catch(e){}
        if(clock) clock.textContent = ('0'+d.getHours()).slice(-2) + ':' + ('0'+d.getMinutes()).slice(-2);
        if(arc){ var h = d.getHours() + d.getMinutes()/60, day = h >= 6 && h < 20;
          var u = day ? (h-6)/14 : ((h+4)%24)/10;  /* ημέρα 06–20, νύχτα 20–06 */
          var x = 6 + 108*u, y = 30 - 38*u*(1-u)*2;
          var c = arc.querySelector('circle'); c.setAttribute('cx', x.toFixed(1)); c.setAttribute('cy', y.toFixed(1));
          arc.classList.toggle('dark', !day); }
      };
      tick(); setInterval(tick, 30000);
    }

    /* παράθυρα: μεγαλώνουν από το πλαίσιο και ξαναμαζεύονται εκεί */
    var from = null;
    function flip(dlg, card, opening){
      if(reduce || !card || !dlg.animate) return null;
      var a = card.getBoundingClientRect(), b = dlg.getBoundingClientRect();
      var sx = a.width / b.width, sy = a.height / b.height;
      var dx = (a.left + a.width/2) - (b.left + b.width/2), dy = (a.top + a.height/2) - (b.top + b.height/2);
      var small = 'translate(' + dx + 'px,' + dy + 'px) scale(' + sx + ',' + sy + ')';
      var frames = [{ transform: small, opacity: .2 }, { transform: 'none', opacity: 1 }];
      return dlg.animate(opening ? frames : frames.slice().reverse(), { duration: opening ? 460 : 340, easing: 'cubic-bezier(.2,.8,.2,1)' });
    }
    document.querySelectorAll('.card[data-w]').forEach(function(card){
      card.addEventListener('click', function(){
        var dlg = document.getElementById('w-' + card.dataset.w); if(!dlg) return;
        from = card; dlg.showModal(); dlg.scrollTop = 0; flip(dlg, card, true);
      });
    });
    function shut(dlg){
      var an = flip(dlg, from, false);
      if(an){ an.onfinish = function(){ dlg.close(); }; } else dlg.close();
    }
    document.querySelectorAll('dialog.win').forEach(function(dlg){
      dlg.querySelector('.wclose').addEventListener('click', function(){ shut(dlg); });
      dlg.addEventListener('click', function(e){ if(e.target === dlg){ var r = dlg.getBoundingClientRect();
        if(e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) shut(dlg); } });
      dlg.addEventListener('cancel', function(e){ e.preventDefault(); shut(dlg); });
      dlg.addEventListener('close', function(){ if(from) from.focus(); });
    });

    /* πρόοδος ανάγνωσης */
    var prog = document.querySelector('.prog'), art = document.querySelector('.post .body');
    if(prog && art){ var tick = false;
      function upd(){ tick = false; var r = art.getBoundingClientRect(), h = r.height - innerHeight * .6;
        var f = h > 0 ? Math.min(1, Math.max(0, -r.top / h)) : 1; prog.style.transform = 'scaleX(' + f.toFixed(4) + ')'; }
      addEventListener('scroll', function(){ if(!tick){ tick = true; requestAnimationFrame(upd); } }, {passive:true});
      addEventListener('resize', upd); upd(); }

    /* χάρτης: ένα σημείο φωτίζει τους γείτονές του */
    var map = document.querySelector('svg.map'), cap = document.querySelector('.cap');
    if(map){
      var lines = map.querySelectorAll('line'), dots = map.querySelectorAll('a[data-i]');
      function show(a){
        var i = a.dataset.i, nb = {}; nb[i] = 1;
        map.classList.add('on');
        lines.forEach(function(l){ var h = l.dataset.a === i || l.dataset.b === i; l.classList.toggle('hl', h); if(h){ nb[l.dataset.a] = 1; nb[l.dataset.b] = 1; } });
        dots.forEach(function(d){ var c = d.firstChild; c.classList.toggle('hl', !!nb[d.dataset.i]); c.classList.toggle('me', d === a); });
        if(cap){ cap.textContent = a.dataset.t; var sm = document.createElement('small'); sm.textContent = a.dataset.d; cap.appendChild(sm); }
      }
      function hide(){ map.classList.remove('on'); }
      var cur = null, touch = false;
      dots.forEach(function(a){
        a.addEventListener('pointerdown', function(e){ touch = e.pointerType !== 'mouse'; });
        a.addEventListener('pointerenter', function(){ show(a); });
        a.addEventListener('focus', function(){ show(a); });
        /* στην αφή: το πρώτο άγγιγμα δείχνει τον τίτλο, το δεύτερο ανοίγει το κείμενο */
        a.addEventListener('click', function(e){ if(touch && cur !== a){ e.preventDefault(); cur = a; show(a); } });
      });
      map.addEventListener('pointerleave', hide);
      setTimeout(function(){ if(window.ivanPanZoom) window.ivanPanZoom(map); }, 0);
    }

    /* αναζήτηση στη βιβλιοθήκη: πρώτα τίτλοι και αρχές, και μέσα σε όλο το κείμενο μόλις φορτωθεί το ευρετήριο */
    var inp = document.querySelector('.search input'); if(!inp) return;
    var none = document.querySelector('.none'), full = null, loading = false;
    function load(){ if(full || loading || !inp.dataset.src || !window.fetch) return; loading = true;
      fetch(inp.dataset.src).then(function(r){ return r.json(); }).then(function(d){
        full = {}; d.forEach(function(e){ full[e.p] = { x: e.x, n: norm(e.x) }; }); run(); }).catch(function(){ loading = false; }); }
    function esc(s){ return s.replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
    function run(){
      var v = norm(inp.value.trim()), any = false;
      document.querySelectorAll('.year').forEach(function(g){
        var c = 0;
        g.querySelectorAll('li').forEach(function(li){
          var sn = li.querySelector('.snip'); if(sn) sn.remove();
          var ok = !v || li.getAttribute('data-k').indexOf(v) >= 0, e = full && full[li.dataset.p];
          if(v.length > 2 && e){ var i = e.n.indexOf(v);
            if(i >= 0){ ok = true; var a0 = Math.max(0, i - 70), a1 = Math.min(e.x.length, i + v.length + 90);
              if(a0){ var s0 = e.x.indexOf(' ', a0); if(s0 > 0 && s0 < i) a0 = s0 + 1; } if(a1 < e.x.length){ var s1 = e.x.lastIndexOf(' ', a1); if(s1 > i + v.length) a1 = s1; }
              var p = document.createElement('p'); p.className = 'snip';
              p.innerHTML = (a0 ? '… ' : '') + esc(e.x.slice(a0, i)) + '<mark>' + esc(e.x.slice(i, i + v.length)) + '</mark>' + esc(e.x.slice(i + v.length, a1)) + (a1 < e.x.length ? ' …' : '');
              li.appendChild(p); } }
          li.hidden = !ok; if(ok) c++;
        });
        g.hidden = !c; if(c) any = true;
      });
      if(none) none.hidden = any;
    }
    inp.addEventListener('focus', load);
    inp.addEventListener('input', function(){ load(); run(); });
  });
})();

/* χάρτης: ολόκληρος στην οθόνη (όρθιος στο κινητό), μετακίνηση και μεγέθυνση με ελαστικά όρια */
window.ivanPanZoom = function(map){
  var box = map.parentNode, vp = map.querySelector('.vp'), tr = map.querySelector('.tr'); if(!vp || !tr) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W0 = +map.dataset.w, H0 = +map.dataset.h, W, H;
  function orient(){ var tall = innerWidth < 704 && innerHeight > innerWidth;
    W = tall ? H0 : W0; H = tall ? W0 : H0;
    map.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    tr.setAttribute('transform', tall ? 'matrix(0 1 1 0 0 0)' : ''); }
  orient();
  var s = 1, x = 0, y = 0, MAXS = 5, vx = 0, vy = 0, raf = 0, moved = false;
  function k(){ return W / box.clientWidth; }
  function limit(v, lo, hi){ return v < lo ? lo : v > hi ? hi : v; }
  function rub(v, lo, hi){ if(v < lo) return lo - (lo - v) * .35; if(v > hi) return hi + (v - hi) * .35; return v; }
  function lo(){ return { x: W - W * s, y: H - H * s }; }
  function apply(){ vp.setAttribute('transform', 'translate(' + x.toFixed(2) + ' ' + y.toFixed(2) + ') scale(' + s.toFixed(4) + ')'); }
  function settle(){ cancelAnimationFrame(raf);
    var step = function(){
      var ts = limit(s, 1, MAXS); if(Math.abs(ts - s) > .001){ var cx = W/2, cy = H/2; x = cx - (cx - x) * (s + (ts - s) * .2) / s; y = cy - (cy - y) * (s + (ts - s) * .2) / s; s += (ts - s) * .2; }
      x += vx; y += vy; vx *= .9; vy *= .9;
      var L = lo(), tx = limit(x, L.x, 0), ty = limit(y, L.y, 0);
      if(tx !== x){ x += (tx - x) * .18; vx *= .5; } if(ty !== y){ y += (ty - y) * .18; vy *= .5; }
      apply();
      if(Math.abs(vx) + Math.abs(vy) > .05 || Math.abs(tx - x) > .3 || Math.abs(ty - y) > .3 || Math.abs(limit(s,1,MAXS) - s) > .002) raf = requestAnimationFrame(step);
      else { s = limit(s, 1, MAXS); var L2 = lo(); x = limit(x, L2.x, 0); y = limit(y, L2.y, 0); apply(); }
    };
    if(reduce){ s = limit(s,1,MAXS); var L = lo(); x = limit(x, L.x, 0); y = limit(y, L.y, 0); apply(); } else raf = requestAnimationFrame(step); }
  function zoomAt(f, cx, cy){ var ns = s * f; ns = ns > MAXS ? MAXS + (ns - MAXS) * .3 : ns < 1 ? 1 - (1 - ns) * .3 : ns;
    x = cx - (cx - x) * ns / s; y = cy - (cy - y) * ns / s; s = ns; apply(); }
  function pt(e){ var r = box.getBoundingClientRect(), kk = k(); return { x: (e.clientX - r.left) * kk, y: (e.clientY - r.top) * kk }; }
  var P = {}, last = null, pinch = null, t0 = 0;
  box.addEventListener('pointerdown', function(e){ P[e.pointerId] = pt(e); cancelAnimationFrame(raf); vx = vy = 0; moved = false; t0 = Date.now();
    var ids = Object.keys(P); if(ids.length === 2){ var a = P[ids[0]], b = P[ids[1]]; pinch = { d: Math.hypot(a.x-b.x, a.y-b.y), m: {x:(a.x+b.x)/2, y:(a.y+b.y)/2} }; }
    last = P[e.pointerId]; });
  box.addEventListener('pointermove', function(e){ if(!(e.pointerId in P)) return; var p = pt(e), ids = Object.keys(P);
    if(ids.length === 2 && pinch){ P[e.pointerId] = p; var a = P[ids[0]], b = P[ids[1]], d = Math.hypot(a.x-b.x, a.y-b.y), m = {x:(a.x+b.x)/2, y:(a.y+b.y)/2};
      zoomAt(d / pinch.d, m.x, m.y); x += m.x - pinch.m.x; y += m.y - pinch.m.y; apply(); pinch = { d: d, m: m }; moved = true; return; }
    var dx = p.x - P[e.pointerId].x, dy = p.y - P[e.pointerId].y;
    if(!moved && Math.hypot(dx, dy) < 6 * k()) return;
    if(!moved){ moved = true; box.classList.add('drag'); try{ box.setPointerCapture(e.pointerId); }catch(_){} }
    var L = lo(); var nx = x + dx, ny = y + dy;
    x = (x < L.x || x > 0) ? x + dx * .35 : rub(nx, L.x, 0); y = (y < L.y || y > 0) ? y + dy * .35 : rub(ny, L.y, 0);
    vx = dx * .6 + vx * .4; vy = dy * .6 + vy * .4; P[e.pointerId] = p; apply(); });
  function up(e){ if(!(e.pointerId in P)) return; delete P[e.pointerId]; pinch = null; box.classList.remove('drag');
    if(Object.keys(P).length === 0) settle(); }
  box.addEventListener('pointerup', up); box.addEventListener('pointercancel', up);
  box.addEventListener('click', function(e){ if(moved){ e.preventDefault(); e.stopPropagation(); moved = false; } }, true);
  box.addEventListener('dblclick', function(e){ e.preventDefault(); var p = pt(e); if(s > 1.5){ vx = vy = 0; var f = 1 / s; zoomAt(f, p.x, p.y); settle(); } else { zoomAt(2.2, p.x, p.y); settle(); } });
  box.addEventListener('wheel', function(e){ if(!e.ctrlKey && !e.metaKey) return; e.preventDefault(); var p = pt(e); zoomAt(Math.exp(-e.deltaY * .004), p.x, p.y); clearTimeout(box._w); box._w = setTimeout(settle, 120); }, {passive:false});
  var z = document.createElement('div'); z.className = 'mapzoom';
  z.innerHTML = '<button type="button" aria-label="Μεγέθυνση">+</button><button type="button" aria-label="Σμίκρυνση">−</button>';
  box.appendChild(z);
  z.addEventListener('pointerdown', function(e){ e.stopPropagation(); });
  z.children[0].addEventListener('click', function(e){ e.stopPropagation(); zoomAt(1.6, W/2, H/2); settle(); });
  z.children[1].addEventListener('click', function(e){ e.stopPropagation(); zoomAt(1/1.6, W/2, H/2); settle(); });
  addEventListener('resize', function(){ var w = W; orient(); if(w !== W){ s = 1; x = y = 0; apply(); } });
  apply();
};

/* σύρσιμο στο κινητό: προς τα αριστερά το επόμενο κείμενο, προς τα δεξιά το προηγούμενο */
(function(){
  if(!('ontouchstart' in window)) return;
  function go(){
    var main = document.querySelector('body.text main.wrap'); if(!main) return;
    var nx = document.querySelector('.pn .nx'), pv = document.querySelector('.pn .pv'); if(!nx && !pv) return;
    var hint = document.createElement('div'); hint.className = 'swipe-hint'; hint.setAttribute('aria-hidden', 'true'); document.body.appendChild(hint);
    var sx = 0, sy = 0, dx = 0, lock = 0, on = false;
    document.addEventListener('touchstart', function(e){ if(e.touches.length !== 1) { on = false; return; } var t = e.touches[0];
      if(t.clientX < 24 || t.clientX > innerWidth - 24 || (e.target.closest && e.target.closest('.mapbox, table, pre'))) { on = false; return; }
      sx = t.clientX; sy = t.clientY; dx = 0; lock = 0; on = true; main.style.transition = 'none'; }, {passive:true});
    document.addEventListener('touchmove', function(e){ if(!on) return; var t = e.touches[0], ddx = t.clientX - sx, ddy = t.clientY - sy;
      if(!lock){ if(Math.abs(ddx) > 14 && Math.abs(ddx) > Math.abs(ddy) * 1.6) lock = 1; else if(Math.abs(ddy) > 10) { lock = -1; } }
      if(lock !== 1) return;
      var target = ddx < 0 ? nx : pv; dx = ddx;
      main.style.transform = 'translateX(' + (ddx * (target ? .32 : .12)).toFixed(1) + 'px)';
      if(target){ hint.textContent = (target.querySelector('small') ? target.querySelector('small').textContent + ' · ' : '') + target.lastChild.textContent;
        hint.className = 'swipe-hint ' + (ddx < 0 ? 'r' : 'l'); hint.style.opacity = Math.min(1, Math.abs(ddx) / 90); }
      else hint.style.opacity = 0; }, {passive:true});
    document.addEventListener('touchend', function(){ if(!on) return; on = false;
      var target = dx < 0 ? nx : pv;
      main.style.transition = 'transform .45s cubic-bezier(.2,.9,.25,1.15)';
      if(lock === 1 && target && Math.abs(dx) > 90){ main.style.transform = 'translateX(' + (dx < 0 ? -40 : 40) + 'px)'; main.style.opacity = '.6'; location.href = target.href; }
      else { main.style.transform = ''; }
      hint.style.opacity = 0; });
    addEventListener('pageshow', function(){ main.style.transform = ''; main.style.opacity = ''; });
  }
  if(document.readyState !== 'loading') go(); else document.addEventListener('DOMContentLoaded', go);
})();
