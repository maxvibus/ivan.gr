/* ήπια κύλιση: δείχνει ότι υπάρχει συνέχεια, χωρίς να «πετά» τον αναγνώστη */
(function(){
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var running = false;
  function ease(t){ return t<.5 ? 4*t*t*t : 1-Math.pow(-2*t+2,3)/2; }
  function glide(target){
    var start = window.scrollY;
    var end = Math.max(0, target.getBoundingClientRect().top + start - window.innerHeight*0.30);
    end = Math.min(end, document.documentElement.scrollHeight - window.innerHeight);
    if (reduce || Math.abs(end-start) < 2){ window.scrollTo(0,end); return; }
    var dur = 1600, t0 = null; running = true;
    function stop(){ running = false; }
    ['wheel','touchstart','keydown','mousedown'].forEach(function(ev){ window.addEventListener(ev, stop, {once:true, passive:true}); });
    function step(ts){
      if (!running) return;
      if (t0 === null) t0 = ts;
      var p = Math.min(1, (ts - t0)/dur);
      window.scrollTo(0, start + (end-start)*ease(p));
      if (p < 1) requestAnimationFrame(step); else running = false;
    }
    requestAnimationFrame(step);
  }
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a.down, a.ek');
    if (!a) return;
    var t = document.getElementById('book'); if (!t) return;
    e.preventDefault(); glide(t);
  });

  /* προς το ivan.gr: η επόμενη σελίδα ξεκινά από την ώχρα και σβήνει στο χαρτί */
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="../"], a[href="/"]');
    if(a){ try{ sessionStorage.setItem('from-ek', '1'); }catch(err){} }
  }, true);

  /* διακόπτης νύχτας, κοινός με το ivan.gr */
  var root = document.documentElement, meta = document.querySelector('meta[name="theme-color"]');
  function sync(){ var n = root.dataset.theme === 'night';
    document.querySelectorAll('button.night').forEach(function(b){ b.setAttribute('aria-pressed', String(n)); b.setAttribute('aria-label', n ? 'Ανάγνωση ημέρας' : 'Νυχτερινή ανάγνωση'); });
    if(meta) meta.setAttribute('content', n ? '#0F1620' : '#EDC89B'); }
  sync();
  document.addEventListener('click', function(e){
    var b = e.target.closest && e.target.closest('button.night'); if(!b) return;
    var n = root.dataset.theme !== 'night';
    if(n) root.dataset.theme = 'night'; else delete root.dataset.theme;
    try{ if(n) localStorage.setItem('ivan-theme','night'); else localStorage.removeItem('ivan-theme'); }catch(err){}
    sync();
  });
})();
