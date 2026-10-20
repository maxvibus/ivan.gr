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
      function flip(){ if(n) root.dataset.theme = 'night'; else delete root.dataset.theme; sync(); }
      try{ if(n) localStorage.setItem('ivan-theme','night'); else localStorage.removeItem('ivan-theme'); }catch(e){}
      /* η μέρα και η νύχτα περνούν η μία στην άλλη αργά, σαν σούρουπο */
      if(!reduce && document.startViewTransition){ root.classList.add('theming');
        var vt = document.startViewTransition(flip); vt.finished.then(function(){ root.classList.remove('theming'); }, function(){ root.classList.remove('theming'); }); }
      else flip();
    }); });

    /* η γραμμή της ημέρας: ημερομηνία και ώρα του αναγνώστη, και ο ήλιος (ή η σελήνη) πάνω στο τόξο της μέρας */
    var dday = document.querySelector('[data-today]'), clock = document.querySelector('[data-clock]');
    if(dday){
      var tick = function(){
        var d = new Date();
        try{ var t = d.toLocaleDateString('el-GR', {weekday:'long', day:'numeric', month:'long', year:'numeric'});
             dday.textContent = t.charAt(0).toUpperCase() + t.slice(1).replace(',', ''); }catch(e){}
        if(clock) clock.textContent = ('0'+d.getHours()).slice(-2) + ':' + ('0'+d.getMinutes()).slice(-2);

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
      var lab2 = document.createElement('div'); lab2.className = 'maplabel'; lab2.hidden = true; lab2.setAttribute('aria-hidden', 'true'); map.parentNode.appendChild(lab2);
      function show(a){
        var i = a.dataset.i, nb = {}; nb[i] = 1;
        map.classList.add('on');
        lines.forEach(function(l){ var h = l.dataset.a === i || l.dataset.b === i; l.classList.toggle('hl', h); if(h){ nb[l.dataset.a] = 1; nb[l.dataset.b] = 1; } });
        dots.forEach(function(d){ var c = d.firstChild; c.classList.toggle('hl', !!nb[d.dataset.i]); c.classList.toggle('me', d === a); });
        map.dispatchEvent(new CustomEvent('ivan-focus', { detail: +i }));
        if(lab2){ var bx = map.parentNode.getBoundingClientRect(), cr = a.firstChild.getBoundingClientRect();
          lab2.innerHTML = ''; var tt = document.createElement('b'); tt.textContent = a.dataset.t; var sm2 = document.createElement('small'); sm2.textContent = a.dataset.d; lab2.append(tt, sm2);
          lab2.hidden = false; placeLabel(lab2, cr.left + cr.width / 2 - bx.left, cr.top - bx.top, bx.width); }
        if(cap){ cap.textContent = a.dataset.t; var sm = document.createElement('small'); sm.textContent = a.dataset.d; cap.appendChild(sm); }
      }
      function hide(){ map.classList.remove('on'); map.dispatchEvent(new Event('ivan-blur')); if(lab2) lab2.hidden = true; }
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

/* χάρτης: ένα με το χαρτί του τετραδίου. Ο κάνναβος είναι μια επιφάνεια που τα κείμενα σηκώνουν σαν τέντα
   (όσο μεγαλύτερο το κείμενο, τόσο ψηλότερα)· ένα σημείο που αγγίζεις σηκώνει περισσότερο το χαρτί γύρω του.
   Στο κινητό η σελίδα κυλά κανονικά· ο χάρτης μετακινείται μόνο όταν έχει μεγεθυνθεί, και μεγεθύνεται με δύο δάχτυλα. */
window.ivanPanZoom = function(map){
  var box = map.parentNode, vp = map.querySelector('.vp'), tr = map.querySelector('.tr'), surf = map.querySelector('.surf'); if(!vp || !tr) return;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches, NS = 'http://www.w3.org/2000/svg';
  var W0 = +map.dataset.w, H0 = +map.dataset.h, W, H, tall = false;
  var links = [].slice.call(tr.querySelectorAll('.nodes a')), C = links.map(function(a){ return a.querySelector('circle'); });
  var L = [].slice.call(tr.querySelectorAll('.edges line'));
  var N0 = C.map(function(c){ return { x: +c.getAttribute('cx'), y: +c.getAttribute('cy'), r: +c.getAttribute('r') }; });
  var lift = N0.map(function(){ return 1; }), goal = N0.map(function(){ return 1; });
  var N = [], gridH = [], gridV = [], G = 28, SIG = 30, PROJ = 1;
  function P(i){ var n = N0[i]; return tall ? { x: n.y, y: n.x, r: n.r } : { x: n.x, y: n.y, r: n.r }; }
  function h(x, y){ var t = 0; for(var i = 0; i < N.length; i++){ var dx = x - N[i].x, dy = y - N[i].y, d2 = dx*dx + dy*dy;
      if(d2 < 9 * SIG * SIG) t += N[i].a * Math.exp(-d2 / (2 * SIG * SIG)); } return Math.min(t, 60); }
  function build(){
    tall = innerWidth < 704 && innerHeight > innerWidth; W = tall ? H0 : W0; H = tall ? W0 : H0;
    map.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    N = N0.map(function(_, i){ var p = P(i); return { x: p.x, y: p.y, r: p.r, a: 0 }; });
    G = Math.max(14, 28 * W / Math.max(1, box.clientWidth));  /* τετραγωνάκια όσο του τετραδίου */
    SIG = G * 1.05;
    while(surf.firstChild) surf.removeChild(surf.firstChild); gridH = []; gridV = [];
    /* οι γραμμές συνεχίζουν ακριβώς τον κάνναβο της σελίδας: ίδια απόσταση, ίδια θέση */
    var r = box.getBoundingClientRect(), kk = W / Math.max(1, r.width), bw = document.body.clientWidth;
    var ox = (((bw / 2 - 14) - (r.left + scrollX)) % 28 + 28) % 28, oy = ((0 - (r.top + scrollY)) % 28 + 28) % 28;
    for(var y = oy * kk; y <= H + .5; y += G){ var e = document.createElementNS(NS, 'path'); surf.appendChild(e); gridH.push({ e: e, v: y }); }
    for(var x = ox * kk; x <= W + .5; x += G){ var e2 = document.createElementNS(NS, 'path'); surf.appendChild(e2); gridV.push({ e: e2, v: x }); }
    draw();
  }
  function draw(){
    for(var i = 0; i < N.length; i++) N[i].a = (1.2 + N[i].r * 1.5) * lift[i];
    var st = G / 3, k, d, pts;
    gridH.forEach(function(g){ d = ''; for(k = -st; k <= W + st; k += st){ var yy = g.v - PROJ * h(k, g.v); d += (d ? 'L' : 'M') + k.toFixed(1) + ' ' + yy.toFixed(1); } g.e.setAttribute('d', d); });
    gridV.forEach(function(g){ d = ''; for(k = -st; k <= H + st; k += st){ var yy = k - PROJ * h(g.v, k); d += (d ? 'L' : 'M') + g.v.toFixed(1) + ' ' + yy.toFixed(1); } g.e.setAttribute('d', d); });
    var Y = N.map(function(n){ return n.y - PROJ * h(n.x, n.y); });
    C.forEach(function(c, i){ c.setAttribute('cx', N[i].x.toFixed(1)); c.setAttribute('cy', Y[i].toFixed(1)); });
    L.forEach(function(l){ var a = +l.dataset.a, b = +l.dataset.b;
      l.setAttribute('x1', N[a].x.toFixed(1)); l.setAttribute('y1', Y[a].toFixed(1)); l.setAttribute('x2', N[b].x.toFixed(1)); l.setAttribute('y2', Y[b].toFixed(1)); });
  }
  /* ανασήκωμα γύρω από το σημείο που αγγίζεις: ήπια, με απόσβεση */
  var araf = 0;
  function animate(){ cancelAnimationFrame(araf);
    var step = function(){ var moving = false;
      for(var i = 0; i < lift.length; i++){ var dl = goal[i] - lift[i]; if(Math.abs(dl) > .01){ lift[i] += dl * .12; moving = true; } else lift[i] = goal[i]; }
      draw(); if(moving) araf = requestAnimationFrame(step); };
    if(reduce){ lift = goal.slice(); draw(); } else araf = requestAnimationFrame(step); }
  map.addEventListener('ivan-focus', function(e){ var i = e.detail, nb = {}; nb[i] = 1;
    L.forEach(function(l){ if(+l.dataset.a === i) nb[+l.dataset.b] = 1; if(+l.dataset.b === i) nb[+l.dataset.a] = 1; });
    goal = N0.map(function(_, j){ return j === i ? 3.2 : nb[j] ? 1.8 : 1; }); animate(); });
  map.addEventListener('ivan-blur', function(){ goal = N0.map(function(){ return 1; }); animate(); });

  /* μετακίνηση και μεγέθυνση */
  var s = 1, x = 0, y = 0, MAXS = 5, vx = 0, vy = 0, raf = 0, moved = false;
  function k(){ return W / box.clientWidth; }
  function limit(v, lo, hi){ return v < lo ? lo : v > hi ? hi : v; }
  function lo(){ return { x: W - W * s, y: H - H * s }; }
  function apply(){ vp.setAttribute('transform', 'translate(' + x.toFixed(2) + ' ' + y.toFixed(2) + ') scale(' + s.toFixed(4) + ')');
    box.classList.toggle('zoomed', s > 1.02); }
  function settle(){ cancelAnimationFrame(raf);
    var step = function(){
      var ts = limit(s, 1, MAXS); if(Math.abs(ts - s) > .001){ var f = (s + (ts - s) * .2) / s; x = W/2 - (W/2 - x) * f; y = H/2 - (H/2 - y) * f; s *= f; }
      x += vx; y += vy; vx *= .9; vy *= .9;
      var B = lo(), tx = limit(x, B.x, 0), ty = limit(y, B.y, 0);
      if(tx !== x){ x += (tx - x) * .18; vx *= .5; } if(ty !== y){ y += (ty - y) * .18; vy *= .5; }
      apply();
      if(Math.abs(vx) + Math.abs(vy) > .05 || Math.abs(tx - x) > .3 || Math.abs(ty - y) > .3 || Math.abs(limit(s,1,MAXS) - s) > .002) raf = requestAnimationFrame(step);
      else { s = limit(s, 1, MAXS); var B2 = lo(); x = limit(x, B2.x, 0); y = limit(y, B2.y, 0); apply(); }
    };
    if(reduce){ s = limit(s,1,MAXS); var B = lo(); x = limit(x, B.x, 0); y = limit(y, B.y, 0); apply(); } else raf = requestAnimationFrame(step); }
  function zoomAt(f, cx, cy){ var ns = s * f; ns = ns > MAXS ? MAXS + (ns - MAXS) * .3 : ns < 1 ? 1 - (1 - ns) * .3 : ns;
    x = cx - (cx - x) * ns / s; y = cy - (cy - y) * ns / s; s = ns; apply(); }
  function pt(e){ var r = box.getBoundingClientRect(), kk = k(); return { x: (e.clientX - r.left) * kk, y: (e.clientY - r.top) * kk }; }
  var Pp = {}, pinch = null;
  box.addEventListener('pointerdown', function(e){ Pp[e.pointerId] = pt(e); cancelAnimationFrame(raf); vx = vy = 0; moved = false;
    var ids = Object.keys(Pp); if(ids.length === 2){ var a = Pp[ids[0]], b = Pp[ids[1]]; pinch = { d: Math.hypot(a.x-b.x, a.y-b.y), m: {x:(a.x+b.x)/2, y:(a.y+b.y)/2} }; } });
  box.addEventListener('pointermove', function(e){ if(!(e.pointerId in Pp)) return; var p = pt(e), ids = Object.keys(Pp);
    if(ids.length === 2 && pinch){ Pp[e.pointerId] = p; var a = Pp[ids[0]], b = Pp[ids[1]], d = Math.hypot(a.x-b.x, a.y-b.y), m = {x:(a.x+b.x)/2, y:(a.y+b.y)/2};
      zoomAt(d / pinch.d, m.x, m.y); x += m.x - pinch.m.x; y += m.y - pinch.m.y; apply(); pinch = { d: d, m: m }; moved = true; return; }
    if(e.pointerType !== 'mouse' && s <= 1.02) return;          /* αμεγέθυντος στην αφή: η σελίδα κυλά, ο χάρτης μένει */
    var dx = p.x - Pp[e.pointerId].x, dy = p.y - Pp[e.pointerId].y;
    if(!moved && Math.hypot(dx, dy) < 6 * k()) return;
    if(!moved){ moved = true; box.classList.add('drag'); try{ box.setPointerCapture(e.pointerId); }catch(_){} }
    var B = lo();
    x = (x < B.x || x > 0) ? x + dx * .35 : x + dx; y = (y < B.y || y > 0) ? y + dy * .35 : y + dy;
    vx = dx * .6 + vx * .4; vy = dy * .6 + vy * .4; Pp[e.pointerId] = p; apply(); });
  function up(e){ if(!(e.pointerId in Pp)) return; delete Pp[e.pointerId]; pinch = null; box.classList.remove('drag');
    if(Object.keys(Pp).length === 0) settle(); }
  box.addEventListener('pointerup', up); box.addEventListener('pointercancel', up);
  box.addEventListener('click', function(e){ if(moved){ e.preventDefault(); e.stopPropagation(); moved = false; } }, true);
  box.addEventListener('dblclick', function(e){ e.preventDefault(); var p = pt(e); if(s > 1.5) zoomAt(1 / s, p.x, p.y); else zoomAt(2.2, p.x, p.y); settle(); });
  box.addEventListener('wheel', function(e){ if(!e.ctrlKey && !e.metaKey) return; e.preventDefault(); var p = pt(e); zoomAt(Math.exp(-e.deltaY * .004), p.x, p.y); clearTimeout(box._w); box._w = setTimeout(settle, 120); }, {passive:false});
  var z = document.createElement('div'); z.className = 'mapzoom';
  z.innerHTML = '<button type="button" aria-label="Μεγέθυνση">+</button><button type="button" aria-label="Σμίκρυνση">−</button>';
  box.appendChild(z);
  z.addEventListener('pointerdown', function(e){ e.stopPropagation(); });
  z.children[0].addEventListener('click', function(e){ e.stopPropagation(); zoomAt(1.6, W/2, H/2); settle(); });
  z.children[1].addEventListener('click', function(e){ e.stopPropagation(); zoomAt(1/1.6, W/2, H/2); settle(); });
  var rt = 0; addEventListener('resize', function(){ clearTimeout(rt); rt = setTimeout(function(){ var t0 = tall; build(); if(t0 !== tall){ s = 1; x = y = 0; } apply(); }, 150); });
  build(); apply();
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

/* το ηλιακό σύστημα της ημέρας: οι πλανήτες στις θέσεις τους σήμερα (μέσες ηλιοκεντρικές αποστάσεις, J2000)
   και κίνηση με τις πραγματικές περιόδους, πολύ αργή· η μόνη κίνηση του ιστότοπου που σταματά με ένα πάτημα */
(function(){
  function go(){
    var btn = document.querySelector('.orrery'); if(!btn) return;
    var svg = btn.querySelector('svg'), orb = svg.querySelector('.orb'), pl = svg.querySelector('.pl'), NS = 'http://www.w3.org/2000/svg';
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    /* μέση ηλιοκεντρική μήκος στις 1.1.2000 (μοίρες), ημερήσια μετατόπιση, απόσταση σε ΑΜ, μέγεθος σημείου */
    var P = [
      ['Ερμής',   252.25032, 4.09233445, 0.387, .8],
      ['Αφροδίτη',181.97910, 1.60213034, 0.723, 1.1],
      ['Γη',      100.46457, 0.98560910, 1.000, 1.2],
      ['Άρης',    355.44657, 0.52402068, 1.524, .95],
      ['Δίας',     34.39645, 0.08308529, 5.203, 1.7],
      ['Κρόνος',   49.95424, 0.03346972, 9.537, 1.5],
      ['Ουρανός', 313.23810, 0.01173129, 19.19, 1.2],
      ['Ποσειδών',304.87997, 0.00598106, 30.07, 1.2]];
    var CX = 66, CY = 16, RX = 63, K = .265;                 /* ελλείψεις: τροχιές ιδωμένες λοξά */
    function rad(a){ return 6 + (RX - 6) * Math.pow(Math.log(1 + a / .3) / Math.log(1 + 30.07 / .3), 1.05); }
    var dots = P.map(function(p, i){
      var r = rad(p[3]), e = document.createElementNS(NS, 'ellipse');
      e.setAttribute('cx', CX); e.setAttribute('cy', CY); e.setAttribute('rx', r.toFixed(1)); e.setAttribute('ry', (r * K + .6).toFixed(1)); orb.appendChild(e);
      var c = document.createElementNS(NS, 'circle'); c.setAttribute('r', p[4]); if(p[0] === 'Γη') c.setAttribute('class', 'earth');
      var t = document.createElementNS(NS, 'title'); t.textContent = p[0]; c.appendChild(t); pl.appendChild(c);
      return { c: c, r: r, p: p };
    });
    var J2000 = Date.UTC(2000, 0, 1, 12), DAY = 864e5;
    var SPEED = 1 / 1.6;                                     /* μία ημέρα κάθε 1,6 δευτερόλεπτα */
    var simDays = (Date.now() - J2000) / DAY, last = null, paused = false, raf = 0, acc = 0;
    try{ paused = localStorage.getItem('ivan-orrery') === 'paused'; }catch(e){}
    function draw(){
      dots.forEach(function(d){
        var L = (d.p[1] + d.p[2] * simDays) * Math.PI / 180;
        var x = CX + d.r * Math.cos(L), y = CY - d.r * K * Math.sin(L);
        d.c.setAttribute('cx', x.toFixed(2)); d.c.setAttribute('cy', y.toFixed(2));
        d.c.style.opacity = Math.sin(L) > 0 ? .55 : 1;     /* πίσω από τον ήλιο λίγο πιο σβηστοί */
      });
    }
    function loop(ts){
      if(last !== null){ var dt = Math.min(.1, (ts - last) / 1000); acc += dt;
        if(acc >= 1 / 24){ simDays += acc * SPEED; acc = 0; draw(); } }
      last = ts; raf = requestAnimationFrame(loop);
    }
    function set(p){ paused = p; btn.setAttribute('aria-pressed', String(p)); btn.classList.toggle('paused', p);
      cancelAnimationFrame(raf); last = null; if(!p && !reduce) raf = requestAnimationFrame(loop); }
    draw(); set(paused || reduce);
    btn.addEventListener('click', function(){ if(reduce) return; set(!paused); try{ localStorage.setItem('ivan-orrery', paused ? 'paused' : 'on'); }catch(e){} });
    document.addEventListener('visibilitychange', function(){ if(document.hidden){ cancelAnimationFrame(raf); } else if(!paused && !reduce){ last = null; raf = requestAnimationFrame(loop); } });
  }
  if(document.readyState !== 'loading') go(); else document.addEventListener('DOMContentLoaded', go);
})();

/* ετικέτα δίπλα στο σημείο: πάνω του, μέσα στα όρια του χάρτη */
function placeLabel(el, x, y, w){
  el.style.left = '0px'; el.style.top = '0px';
  var lw = el.offsetWidth, lh = el.offsetHeight;
  var lx = Math.max(6, Math.min(w - lw - 6, x - lw / 2)), ly = y - lh - 12;
  if(ly < 6) ly = y + 18;
  el.style.left = lx + 'px'; el.style.top = ly + 'px';
}

/* ο χάρτης στον χώρο: τα κείμενα ως σημεία σε τρεις διαστάσεις, πάνω από το χαρτί του τετραδίου.
   Γυρίζει πολύ αργά μόνος του· σύρσιμο οριζόντια τον στρέφει (η σελίδα κυλά κανονικά κατακόρυφα),
   άγγιγμα σε σημείο δείχνει τον τίτλο του, δεύτερο άγγιγμα ανοίγει το κείμενο. */
(function(){
  function go(){
    var data = document.getElementById('map3d'), box = document.querySelector('.mapbox3'), box2 = document.querySelector('.mapbox'), modes = document.querySelector('.mapmode');
    if(!data || !box || !modes) return;
    var D = JSON.parse(data.textContent), Nn = D.n, Ee = D.e, cv = box.querySelector('canvas'), lab = box.querySelector('.maplabel'), cap = document.querySelector('.cap');
    var ctx = cv.getContext('2d'), reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    var nb = Nn.map(function(){ return []; }); Ee.forEach(function(e){ nb[e[0]].push(e[1]); nb[e[1]].push(e[0]); });
    var yaw = .6, pitch = .38, zoom = 1, W = 0, H = 0, dpr = 1, sel = -1, hov = -1, idleUntil = 0, running = false, last = null, raf = 0, visible = true;
    var P = Nn.map(function(){ return { x: 0, y: 0, z: 0, f: 1 }; });
    function size(){ dpr = Math.min(2, window.devicePixelRatio || 1); W = box.clientWidth; H = Math.round(Math.min(W * (innerWidth < 704 ? 1.15 : .62), innerHeight * .78));
      cv.width = W * dpr; cv.height = H * dpr; cv.style.height = H + 'px'; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); draw(); }
    function proj(x, y, z){
      var cy = Math.cos(yaw), sy = Math.sin(yaw), cp = Math.cos(pitch), sp = Math.sin(pitch);
      var x1 = x * cy - z * sy, z1 = x * sy + z * cy;
      var y2 = y * cp - z1 * sp, z2 = y * sp + z1 * cp;
      var R = Math.min(W, H) * .6 * zoom, f = 3.4 / (3.4 + z2);
      return { x: W / 2 + x1 * R * f, y: H / 2 + y2 * R * f, z: z2, f: f };
    }
    function css(v){ return getComputedStyle(document.documentElement).getPropertyValue(v).trim(); }
    function draw(){
      if(!W) return;
      var blue = css('--blue'), blue2 = css('--blue2'), ochre = css('--ochre'), grid = css('--grid'), rule = css('--rule');
      var night = document.documentElement.dataset.theme === 'night';
      ctx.clearRect(0, 0, W, H);
      /* το χαρτί από κάτω: κάνναβος σε προοπτική */
      ctx.lineWidth = 1; ctx.strokeStyle = night ? 'rgba(141,187,234,.10)' : 'rgba(0,94,171,.11)';
      var FY = 1.12, G = 1.2, st = .12;
      ctx.beginPath();
      for(var g = -G; g <= G + 1e-6; g += st){ var a = proj(g, FY, -G), b = proj(g, FY, G); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y);
        var c = proj(-G, FY, g), d = proj(G, FY, g); ctx.moveTo(c.x, c.y); ctx.lineTo(d.x, d.y); }
      ctx.stroke();
      for(var i = 0; i < Nn.length; i++){ var q = proj(Nn[i][0], Nn[i][1] * .9, Nn[i][2]); P[i] = q; }
      var on = sel >= 0 ? sel : hov, mark = {}; if(on >= 0){ mark[on] = 1; nb[on].forEach(function(j){ mark[j] = 1; }); }
      /* σκιές πάνω στο χαρτί, και για το επιλεγμένο μια κάθετος ως εκεί */
      ctx.fillStyle = night ? 'rgba(141,187,234,.16)' : 'rgba(0,94,171,.13)';
      for(i = 0; i < Nn.length; i++){ var fl = proj(Nn[i][0], FY, Nn[i][2]); ctx.beginPath(); ctx.ellipse(fl.x, fl.y, 2.2 * fl.f, .9 * fl.f, 0, 0, 6.2832); ctx.fill();
        if(mark[i]){ ctx.strokeStyle = night ? 'rgba(237,200,155,.35)' : 'rgba(201,154,94,.45)'; ctx.setLineDash([2, 4]); ctx.beginPath(); ctx.moveTo(P[i].x, P[i].y); ctx.lineTo(fl.x, fl.y); ctx.stroke(); ctx.setLineDash([]); } }
      /* ακμές */
      Ee.forEach(function(e){ var a = P[e[0]], b = P[e[1]], hl = on >= 0 && (e[0] === on || e[1] === on);
        var depth = Math.max(.25, Math.min(1, ((a.f + b.f) / 2 - .72) * 2.4));
        ctx.globalAlpha = hl ? 1 : (on >= 0 ? .14 : .5 * depth);
        ctx.strokeStyle = hl ? (night ? ochre : '#C99A5E') : rule; ctx.lineWidth = hl ? 1.8 : 1;
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); });
      /* σημεία, από τα πίσω προς τα μπρος */
      var order = P.map(function(_, i){ return i; }).sort(function(a, b){ return P[b].z - P[a].z; });
      order.forEach(function(i){ var q = P[i], n = Nn[i], r = Math.max(1.6, n[3] * .62 * q.f * Math.sqrt(zoom));
        var depth = Math.max(.45, Math.min(1, (q.f - .7) * 2.6));
        ctx.globalAlpha = on >= 0 ? (mark[i] ? 1 : .25) : (n[4] >= 2026 ? 1 : .75) * depth;
        ctx.fillStyle = i === on ? (night ? ochre : '#C99A5E') : (n[4] >= 2026 ? blue : blue2);
        ctx.beginPath(); ctx.arc(q.x, q.y, r, 0, 6.2832); ctx.fill(); });
      ctx.globalAlpha = 1;
      if(on >= 0 && !lab.hidden) placeLabel(lab, P[on].x, P[on].y - 6, W);
    }
    function loop(ts){
      if(last !== null && !reduce && Date.now() > idleUntil) yaw += Math.min(.05, (ts - last) / 1000) * .045;
      last = ts; draw(); raf = requestAnimationFrame(loop);
    }
    function start(){ if(running || !visible || box.hidden || document.hidden) return; running = true; last = null; raf = requestAnimationFrame(loop); }
    function stop(){ running = false; cancelAnimationFrame(raf); }
    function pick(x, y){ var best = -1, bd = 22 * 22; for(var i = 0; i < P.length; i++){ var dx = P[i].x - x, dy = P[i].y - y, d = dx*dx + dy*dy; if(d < bd){ bd = d; best = i; } } return best; }
    function show(i){ sel = i; if(i < 0){ lab.hidden = true; return; }
      var n = Nn[i]; lab.innerHTML = ''; var a = document.createElement('a'); a.href = n[7]; a.textContent = n[5]; var sm = document.createElement('small'); sm.textContent = n[6];
      lab.append(a, sm); lab.hidden = false; placeLabel(lab, P[i].x, P[i].y - 6, W);
      if(cap){ cap.textContent = n[5]; var c2 = document.createElement('small'); c2.textContent = n[6]; cap.appendChild(c2); } draw(); }
    /* αφή και ποντίκι */
    var down = null, moved = false, pinch = null, pts = {};
    function xy(e){ var r = cv.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; }
    cv.addEventListener('pointerdown', function(e){ pts[e.pointerId] = xy(e); down = xy(e); moved = false; idleUntil = Date.now() + 6000;
      var ids = Object.keys(pts); if(ids.length === 2){ var a = pts[ids[0]], b = pts[ids[1]]; pinch = Math.hypot(a.x - b.x, a.y - b.y); } });
    cv.addEventListener('pointermove', function(e){ var p = xy(e);
      if(!(e.pointerId in pts)){ if(e.pointerType === 'mouse'){ var h = pick(p.x, p.y); if(h !== hov){ hov = h; cv.style.cursor = h >= 0 ? 'pointer' : 'grab'; if(!running) draw(); } } return; }
      var ids = Object.keys(pts);
      if(ids.length === 2 && pinch){ pts[e.pointerId] = p; var a = pts[ids[0]], b = pts[ids[1]], d = Math.hypot(a.x - b.x, a.y - b.y);
        zoom = Math.max(.7, Math.min(3.2, zoom * d / pinch)); pinch = d; moved = true; if(!running) draw(); return; }
      var q = pts[e.pointerId], dx = p.x - q.x, dy = p.y - q.y;
      if(!moved && Math.hypot(p.x - down.x, p.y - down.y) < 6) return;
      moved = true; idleUntil = Date.now() + 6000;
      yaw += dx * .008; if(e.pointerType === 'mouse') pitch = Math.max(-.2, Math.min(1.2, pitch + dy * .006));
      pts[e.pointerId] = p; if(!running) draw(); });
    function up(e){ if(!(e.pointerId in pts)) return; delete pts[e.pointerId]; pinch = null;
      if(!moved && Object.keys(pts).length === 0){ var p = xy(e), i = pick(p.x, p.y);
        if(i >= 0 && i === sel){ location.href = Nn[i][7]; return; } show(i); } }
    cv.addEventListener('pointerup', up); cv.addEventListener('pointercancel', function(e){ delete pts[e.pointerId]; pinch = null; });
    cv.addEventListener('pointerleave', function(){ if(hov >= 0){ hov = -1; if(!running) draw(); } });
    cv.addEventListener('wheel', function(e){ if(!e.ctrlKey && !e.metaKey) return; e.preventDefault(); zoom = Math.max(.7, Math.min(3.2, zoom * Math.exp(-e.deltaY * .003))); if(!running) draw(); }, {passive:false});
    if('IntersectionObserver' in window) new IntersectionObserver(function(es){ visible = es[0].isIntersecting; if(visible) start(); else stop(); }).observe(box);
    document.addEventListener('visibilitychange', function(){ if(document.hidden) stop(); else start(); });
    var rt = 0; addEventListener('resize', function(){ clearTimeout(rt); rt = setTimeout(function(){ if(!box.hidden) size(); }, 150); });
    /* επίπεδο ή χώρος */
    function mode(m){ var three = m === '3d';
      modes.querySelectorAll('button').forEach(function(b){ b.setAttribute('aria-pressed', String(b.dataset.m === m)); });
      box.hidden = !three; if(box2) box2.hidden = three;
      try{ localStorage.setItem('ivan-map-mode', m); }catch(e){}
      if(three){ size(); start(); } else stop(); }
    modes.addEventListener('click', function(e){ var b = e.target.closest('button'); if(b) mode(b.dataset.m); });
    var m0 = '2d'; try{ m0 = localStorage.getItem('ivan-map-mode') || '2d'; }catch(e){}
    mode(m0);
  }
  if(document.readyState !== 'loading') go(); else document.addEventListener('DOMContentLoaded', go);
})();
