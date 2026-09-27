(function(){
  var root=document.getElementById('du-app');
  if(!root)return;
  root.classList.add('du-js');
  var WA='918595565628';
  var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s,c){return (c||root).querySelector(s)}
  function $$(s,c){return Array.prototype.slice.call((c||root).querySelectorAll(s))}
  function waLink(msg){return 'https://wa.me/'+WA+'?text='+encodeURIComponent(msg)}

  /* ---------- Reveal on scroll ---------- */
  var items=$$('[data-du-reveal]');
  if(reduced||!('IntersectionObserver' in window)){items.forEach(function(el){el.classList.add('du-visible')})}
  else{
    var io=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('du-visible');io.unobserve(e.target)}})},{threshold:.1,rootMargin:'0px 0px -5% 0px'});
    items.forEach(function(el){io.observe(el)});
  }

  /* ---------- FAQ: one open at a time ---------- */
  $$('.du-faq').forEach(function(item){item.addEventListener('toggle',function(){if(!item.open)return;$$('.du-faq[open]').forEach(function(o){if(o!==item)o.removeAttribute('open')})})});

  /* ---------- Hero slider ---------- */
  var slider=$('[data-du-slider]');
  if(slider){
    var slides=$$('.du-slide',slider),dots=$$('.du-slider-dot',slider),toggle=$('.du-slider-toggle',slider);
    var cur=0,timer=null,DELAY=6500,paused=reduced,hovering=false;
    slider.style.setProperty('--du-slide-delay',DELAY+'ms');
    function go(i,user){
      i=(i+slides.length)%slides.length;
      slides.forEach(function(s,k){
        var on=k===i;s.classList.toggle('is-active',on);s.setAttribute('aria-hidden',on?'false':'true');
        if('inert' in s)s.inert=!on;
        if(on){var img=s.querySelector('img[data-src]');if(img){img.src=img.getAttribute('data-src');img.removeAttribute('data-src')}}
      });
      dots.forEach(function(d,k){d.classList.toggle('is-active',k===i);d.setAttribute('aria-current',k===i?'true':'false')});
      cur=i;
      /* restart the progress animation on the active dot */
      slider.classList.remove('is-ticking');void slider.offsetWidth;if(!paused&&!hovering)slider.classList.add('is-ticking');
      if(user)restart();
    }
    function preloadNext(){var n=slides[(cur+1)%slides.length].querySelector('img[data-src]');if(n){n.src=n.getAttribute('data-src');n.removeAttribute('data-src')}}
    function stop(){clearInterval(timer);timer=null;slider.classList.remove('is-ticking')}
    function start(){stop();if(paused||hovering||document.hidden)return;slider.classList.add('is-ticking');timer=setInterval(function(){go(cur+1)},DELAY);setTimeout(preloadNext,1500)}
    function restart(){start()}
    $('.du-slider-prev',slider).addEventListener('click',function(){go(cur-1,true)});
    $('.du-slider-next',slider).addEventListener('click',function(){go(cur+1,true)});
    dots.forEach(function(d,k){d.addEventListener('click',function(){go(k,true)})});
    if(toggle)toggle.addEventListener('click',function(){paused=!paused;toggle.setAttribute('aria-pressed',paused?'true':'false');toggle.setAttribute('aria-label',paused?'Play slideshow':'Pause slideshow');slider.classList.toggle('is-paused',paused);paused?stop():start()});
    slider.addEventListener('mouseenter',function(){hovering=true;stop()});
    slider.addEventListener('mouseleave',function(){hovering=false;start()});
    slider.addEventListener('focusin',function(){hovering=true;stop()});
    slider.addEventListener('focusout',function(e){if(!slider.contains(e.relatedTarget)){hovering=false;start()}});
    slider.addEventListener('keydown',function(e){if(e.key==='ArrowLeft'){go(cur-1,true)}else if(e.key==='ArrowRight'){go(cur+1,true)}});
    document.addEventListener('visibilitychange',function(){document.hidden?stop():start()});
    /* touch swipe */
    var sx=0,sy=0,tracking=false;
    slider.addEventListener('touchstart',function(e){var t=e.touches[0];sx=t.clientX;sy=t.clientY;tracking=true},{passive:true});
    slider.addEventListener('touchend',function(e){if(!tracking)return;tracking=false;var t=e.changedTouches[0],dx=t.clientX-sx,dy=t.clientY-sy;if(Math.abs(dx)>45&&Math.abs(dx)>Math.abs(dy)*1.3){go(cur+(dx<0?1:-1),true)}},{passive:true});
    if(paused){slider.classList.add('is-paused');if(toggle){toggle.setAttribute('aria-pressed','true');toggle.setAttribute('aria-label','Play slideshow')}}
    go(0);start();
  }

  /* ---------- Quick Look modal ---------- */
  var dataEl=document.getElementById('du-services-data'),modal=$('.du-modal');
  if(dataEl&&modal){
    var services={};try{services=JSON.parse(dataEl.textContent)}catch(e){}
    var present=$$('[data-du-quick]').map(function(b){return b.getAttribute('data-du-quick')});
    var order=Object.keys(services).filter(function(k){return present.indexOf(k)>-1});
    var panel=$('.du-modal-panel',modal),lastFocus=null,active=null,scrollY=0;
    function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
    function list(arr){return arr.map(function(t){return '<li><svg aria-hidden="true"><use href="#dui-check"></use></svg>'+esc(t)+'</li>'}).join('')}
    function chips(arr){return arr.map(function(t){return '<span class="du-chip">'+esc(t)+'</span>'}).join('')}
    function fill(slug){
      var s=services[slug];if(!s)return false;active=slug;
      $('.du-modal-media img',modal).src=s.img;$('.du-modal-media img',modal).alt=s.alt||'';
      $('[data-m="label"]',modal).textContent=s.label;
      $('[data-m="name"]',modal).textContent=s.name;
      $('[data-m="tagline"]',modal).textContent=s.tagline;
      $('[data-m="overview"]',modal).textContent=s.overview;
      $('[data-m="included"]',modal).innerHTML=list(s.included);
      $('[data-m="steps"]',modal).innerHTML=s.steps.map(function(st){return '<li><strong>'+esc(st[0])+'</strong>'+esc(st[1])+'</li>'}).join('');
      $('[data-m="ideal"]',modal).innerHTML=chips(s.ideal);
      $('[data-m="metrics"]',modal).innerHTML=chips(s.metrics);
      var page=$('[data-m="page"]',modal);page.href=s.url;page.setAttribute('aria-label','View full details: '+s.name);
      $('[data-m="wa"]',modal).href=waLink('Hello Digital Udyami, I would like to discuss '+s.name+' for my business.');
      $('.du-modal-scroll',modal).scrollTop=0;
      var n=order.length;$('.du-modal-nav',modal).style.display=n>1?'':'none';
      return true;
    }
    function open(slug,trigger){
      if(!fill(slug))return;
      lastFocus=trigger||document.activeElement;
      scrollY=window.pageYOffset;document.documentElement.style.overflow='hidden';document.body.style.overflow='hidden';
      modal.classList.add('is-open');modal.setAttribute('aria-hidden','false');
      setTimeout(function(){$('.du-modal-close',modal).focus({preventScroll:true})},60);
      if(window.dataLayer)window.dataLayer.push({event:'du_quick_look',service:slug});
    }
    function close(){
      if(!modal.classList.contains('is-open'))return;
      modal.classList.remove('is-open');modal.setAttribute('aria-hidden','true');
      document.documentElement.style.overflow='';document.body.style.overflow='';window.scrollTo(0,scrollY);
      if(lastFocus&&lastFocus.focus)lastFocus.focus({preventScroll:true});
    }
    function step(d){var i=order.indexOf(active);fill(order[(i+d+order.length)%order.length])}
    root.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-du-quick]');if(b){e.preventDefault();open(b.getAttribute('data-du-quick'),b)}});
    $$('[data-du-close]',modal).forEach(function(b){b.addEventListener('click',close)});
    $('[data-m="prev"]',modal).addEventListener('click',function(){step(-1)});
    $('[data-m="next"]',modal).addEventListener('click',function(){step(1)});
    document.addEventListener('keydown',function(e){
      if(!modal.classList.contains('is-open'))return;
      if(e.key==='Escape'){close();return}
      if(e.key==='Tab'){
        var f=$$('a[href],button:not([disabled])',panel).filter(function(el){return el.offsetParent!==null});
        if(!f.length)return;var first=f[0],last=f[f.length-1];
        if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
        else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}
      }
    });
    /* swipe down to close the bottom sheet on phones */
    var ty=0;
    $('.du-modal-media',modal).addEventListener('touchstart',function(e){ty=e.touches[0].clientY},{passive:true});
    $('.du-modal-media',modal).addEventListener('touchend',function(e){if(e.changedTouches[0].clientY-ty>70)close()},{passive:true});
    /* deep link: /#quick-look-seo-services */
    var m=location.hash.match(/^#quick-look-(.+)$/);if(m&&services[m[1]])setTimeout(function(){open(m[1])},400);
  }

  /* ---------- Lead forms → WhatsApp ---------- */
  $$('form[data-du-form]').forEach(function(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      if(form.reportValidity&&!form.reportValidity())return;
      var lines=['Hello Digital Udyami, '+(form.getAttribute('data-du-intro')||'I want to discuss a digital growth requirement.'),''];
      $$('[name]',form).forEach(function(f){
        var label=form.querySelector('label[for="'+f.id+'"]');var v=(f.value||'').trim();
        lines.push((label?label.textContent:f.name)+': '+(v||'Not shared'));
      });
      var status=$('.du-form-status',form);if(status)status.textContent='WhatsApp is opening with your prepared message.';
      if(window.dataLayer)window.dataLayer.push({event:'du_lead_form',form:form.id});
      window.open(waLink(lines.join('\n')),'_blank','noopener');
    });
  });

  /* ---------- Mobile action bar: show after the first screen ---------- */
  var bar=$('.du-mobile-bar');
  if(bar){
    var ticking=false;
    function check(){ticking=false;bar.classList.toggle('is-visible',window.pageYOffset>window.innerHeight*.6)}
    window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(check)}},{passive:true});
    check();
  }
})();
/* ---------- Legal pages: table of contents scrollspy + print ---------- */
(function(){
  var root=document.getElementById('du-app');if(!root)return;
  var toc=root.querySelector('.du-toc');
  root.querySelectorAll('[data-du-print]').forEach(function(b){b.addEventListener('click',function(){window.print()})});
  root.querySelectorAll('.du-toc-mobile a').forEach(function(a){a.addEventListener('click',function(){var d=a.closest('details');if(d)d.open=false})});
  if(!toc)return;
  var links={};toc.querySelectorAll('a').forEach(function(a){links[a.getAttribute('href').slice(1)]=a});
  var secs=Array.prototype.slice.call(root.querySelectorAll('.du-legal-section')),cur=null,tick=false;
  function spy(){
    tick=false;var id=secs.length?secs[0].id:null;
    secs.forEach(function(s){if(s.getBoundingClientRect().top<=160)id=s.id});
    if((window.innerHeight+window.pageYOffset)>=document.documentElement.scrollHeight-4)id=secs[secs.length-1].id;
    if(id===cur)return;cur=id;
    Object.keys(links).forEach(function(k){links[k].classList.toggle('is-active',k===id)});
    var a=links[id];if(a&&toc.scrollHeight>toc.clientHeight){var t=a.offsetTop-toc.clientHeight/2;toc.scrollTo({top:t<0?0:t})}
  }
  window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(spy)}},{passive:true});
  spy();
})();
