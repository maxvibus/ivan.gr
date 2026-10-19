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
