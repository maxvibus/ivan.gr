/* ivan.gr — νύχτα/ημέρα, παράθυρα που ανοίγουν από το πλαίσιο, αναζήτηση */
(function(){
  var root = document.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function norm(s){ return (s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/ς/g,'σ'); }

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

    /* αναζήτηση στη βιβλιοθήκη */
    var inp = document.querySelector('.search input'); if(!inp) return;
    var none = document.querySelector('.none');
    inp.addEventListener('input', function(){
      var v = norm(inp.value.trim()), any = false;
      document.querySelectorAll('.year').forEach(function(g){
        var c = 0;
        g.querySelectorAll('li').forEach(function(li){ var ok = !v || li.getAttribute('data-k').indexOf(v) >= 0; li.hidden = !ok; if(ok) c++; });
        g.hidden = !c; if(c) any = true;
      });
      if(none) none.hidden = any;
    });
  });
})();
