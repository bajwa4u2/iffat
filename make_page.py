# Iffat S. Chaudhry, Strategic Member: his room in the company's house (The Record).
# Rules from the founder (2 Oct 2026): no timeline, his own voice, and his role at
# Aura Platform = legal and regulatory judgement, correspondence alongside the founder,
# approaching clients and institutions for the products. No personal address or phone.
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = ('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400'
         '&family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap')
SCRIPTS = 'https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu&display=swap'
CO = 'https://company.auraplatform.org'
URL = 'https://iffat.auraplatform.org/'
TITLE = 'Iffat S. Chaudhry | Strategic Member, Aura Platform LLC'
DESC = ('Iffat S. Chaudhry, Strategic Member of Aura Platform LLC: legal and regulatory judgement, '
        'correspondence alongside the founder, and the first conversation with clients and institutions.')

LD = {"@context": "https://schema.org", "@type": "ProfilePage", "@id": URL + "#profilepage", "url": URL,
      "mainEntity": {"@type": "Person", "@id": URL + "#person", "name": "Iffat S. Chaudhry", "jobTitle": "Strategic Member",
                     "description": "Advocate of the High Court in Lahore and licensed insurance agent in Michigan; Strategic Member of Aura Platform LLC.",
                     "address": {"@type": "PostalAddress", "addressLocality": "Taylor", "addressRegion": "MI", "addressCountry": "US"},
                     "worksFor": {"@type": "Organization", "@id": CO + "/#organization", "name": "Aura Platform LLC", "url": CO + "/"},
                     "sameAs": ["https://www.linkedin.com/in/isch13"],
                     "knowsLanguage": ["pa", "ur", "en"],
                     "knowsAbout": ["Law and advocacy", "Regulatory judgement", "Legal aid", "Insurance", "Correspondence with institutions"]}}

def word(text, lang, d, gloss):
    return f'<span class="word" lang="{lang}" dir="{d}"><b>{text}</b><small lang="en" dir="ltr">{gloss}</small></span>'

body = f'''<section class="hero" id="presence"><div class="wrap split">
  <div>
    <div class="ey">Strategic Member · Aura Platform LLC</div>
    <h1 class="h1">Law, advocacy and <em class="tl">regulated services.</em></h1>
    <p class="lede">I practised law before the High Court in Lahore, led legal aid for children, and today help families and businesses in Michigan protect what they have. At Aura Platform I bring that judgement to the work, alongside the founder.</p>
    <div class="btns"><a class="b1 tlbg" href="#with-aura">What I do at Aura Platform</a><a class="b2" href="#conversation">Write to me</a></div>
  </div>
  <figure class="portrait"><img src="assets/images/leadership/iffat.png" alt="Iffat S. Chaudhry" width="1200" height="1600"><figcaption><b>Iffat S. Chaudhry</b>Strategic Member, Aura Platform LLC · Michigan</figcaption></figure>
</div></section>

<section class="sec" id="with-aura"><div class="wrap">
  <div class="ey">At Aura Platform</div>
  <h2 class="h2">Three things I do <em class="tl">with the founder.</em></h2>
  <p class="swipe-hint" aria-hidden="true">Swipe →</p>
  <div class="carry">
    <div class="cc">
      <div class="mini-stage s-col"><span class="ed"><b>Who agreed?</b> · <b>Who answers?</b><br><span>What can be shown later?</span></span></div>
      <h3>Legal and regulatory judgement.</h3>
      <p>Before something goes out, I ask the questions a court or a regulator would ask. Who is responsible, what was agreed, and what can be shown later.</p>
    </div>
    <div class="cc">
      <div class="mini-stage s-orc"><span class="path"><i class="d">Drafted</i><i class="d">Read by two</i><i class="n">Sent</i></span></div>
      <h3>Correspondence, alongside Muhammad.</h3>
      <p>I write and answer with the founder: letters to institutions, partners and clients, worded with the care a legal letter deserves.</p>
    </div>
    <div class="cc">
      <div class="mini-stage s-aura"><span class="bubble">A first conversation</span><span class="bubble me">Introduced</span></div>
      <h3>The first conversation with clients and institutions.</h3>
      <p>I open doors for our products: businesses for <a href="{CO}/orchestrate">Orchestrate</a>, institutions for <a href="{CO}/aura">Aura</a>, authors and readers for <a href="{CO}/colophon">Colophon</a>.</p>
    </div>
  </div>
</div></section>

<section class="sec" id="law"><div class="wrap split">
  <div>
    <div class="ey">Where it comes from · Lahore</div>
    <h2 class="h2">Inside <em class="tl">formal systems.</em></h2>
    <p class="lede">As an advocate of the High Court I drafted contracts and pleadings, gave legal opinions, corresponded with government departments and represented clients before courts and tribunals. Managing a legal-aid programme for children who survived violence, I worked with the police, the prosecution, the provincial ombudsman, the bar councils and the prison department, so that a child's case could move.</p>
  </div>
  <div class="stage s-co creds" data-name="Bar memberships">
    <ul>
      <li><b>Lahore High Court Bar Association</b></li>
      <li><b>Punjab Bar Council</b></li>
      <li><b>Lahore Bar Association</b></li>
      <li><b>American Bar Association</b></li>
    </ul>
  </div>
</div></section>

<section class="sec" id="insurance"><div class="wrap split">
  <div>
    <div class="ey">Where it comes from · Michigan</div>
    <h2 class="h2">Where the stakes are <em class="tl">personal.</em></h2>
    <p class="lede">Today I run Insure3212 in Taylor as a licensed insurance agent: auto, home, commercial truck and business cover. I compare options across insurers and explain them plainly, because a policy protects a family or a livelihood.</p>
  </div>
  <div class="stage s-co words" data-name="Languages I work in" data-needs-scripts>{word('پنجابی', 'pa-Arab', 'rtl', 'Punjabi')}{word('اردو', 'ur', 'rtl', 'Urdu')}{word('English', 'en', 'ltr', 'English')}</div>
</div></section>

<section class="hero convo2" id="conversation"><div class="wrap split" data-convo data-mailto="iffat@auraplatform.org" data-salute="Iffat">
  <div class="c-left">
    <div class="ey">Write to me</div>
    <h2 class="h1">Talk it through <em class="tone">with me.</em></h2>
    <div class="founder-line"><img src="assets/images/leadership/iffat.png" alt="" width="56" height="56"><p><b>I read every note myself</b> and reply personally.</p></div>
    <p class="origin" data-origin hidden></p>
    <div class="c-tabs" role="tablist" aria-label="Why are you writing?">
      <button type="button" role="tab" data-intent="legal" aria-selected="false">A legal question</button>
      <button type="button" role="tab" data-intent="product" aria-selected="false">A product for my business</button>
      <button type="button" role="tab" data-intent="partnership" aria-selected="false">Partner</button>
      <button type="button" role="tab" data-intent="insurance" aria-selected="false">Insurance</button>
      <button type="button" role="tab" data-intent="unsure" aria-selected="false">Something else</button>
    </div>
    <div class="c-direct" data-direct hidden></div>
  </div>
  <div class="stage s-letter" data-name="Your note">
    <form class="letter-card" data-letter novalidate>
      <div class="lh"><span><b>A personal note</b><small>Read by me, answered by me</small></span><span data-date></span></div>
      <div class="lto"><small>To</small> Iffat S. Chaudhry · Aura Platform LLC</div>
      <div class="lsubj"><small>About</small> <span data-subject>A conversation</span></div>
      <div class="lbody" data-body></div>
      <button type="button" class="lmore" data-more aria-expanded="false" aria-controls="c-detail">Bringing something specific? <u>Add the details.</u></button>
      <div class="ldetail" id="c-detail" data-detail hidden>
        <label><small>What I'm bringing</small><textarea name="bringing" rows="1" placeholder="The question, product or proposal, in a line or two"></textarea></label>
        <label><small>Why now</small><textarea name="pitch" rows="2" placeholder="What makes this the right moment"></textarea></label>
        <label><small>A good first outcome would be</small><textarea name="outcome" rows="1" placeholder="The first thing that would show it is working"></textarea></label>
      </div>
      <div class="lsign"><span>With regards,</span><input name="name" id="c-name" autocomplete="name" required placeholder="Your name" aria-label="Your name"></div>
      <div class="lact"><button class="b1 tonebg" type="submit">Open in my email ↗</button><a class="b2" href="https://auraplatform.org/i/aura-platform-llc/meet/introduction-discussion" target="_blank" rel="noopener">Or choose a time to talk ↗</a></div>
      <div class="attr" data-status><i></i><span>Sent from your own email. The note stays yours.</span></div>
    </form>
  </div>
</div></section>'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta name="author" content="Iffat S. Chaudhry">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="profile"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{DESC}"><meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}assets/social/og-default.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{URL}assets/social/og-default.png">
<link rel="icon" href="favicon.ico"><link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}"><meta name="script-fonts" content="{SCRIPTS}">
<link rel="stylesheet" href="record.css"><link rel="stylesheet" href="member.css">
<script type="application/ld+json">{json.dumps(LD, ensure_ascii=False)}</script>
</head>
<body class="record founder member">
<a class="skip-link" href="#main">Skip to content</a>
<header class="rh fh-head" role="banner">
  <div class="wrap">
    <a class="rh-brand" href="#presence" aria-label="Iffat S. Chaudhry"><img src="assets/images/leadership/iffat.png" alt="" width="28" height="28">Iffat S. Chaudhry</a>
    <nav class="rh-nav" aria-label="Primary">
      <a href="#with-aura">At Aura Platform</a><a href="#law">Law</a><a href="#insurance">Insurance</a><a href="{CO}" rel="noopener">Aura Platform LLC ↗</a>
    </nav>
    <a class="rh-cta" href="#conversation">Write to me</a>
    <button class="rh-menu" type="button" aria-expanded="false" aria-controls="rh-panel"><span></span><b class="sr-only">Menu</b></button>
  </div>
  <nav class="rh-panel" id="rh-panel" aria-label="Mobile primary">
    <a href="#with-aura">At Aura Platform</a><a href="#law">Law</a><a href="#insurance">Insurance</a><a href="{CO}" rel="noopener">Aura Platform LLC ↗</a><a href="#conversation">Write to me</a>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="founder-footer" role="contentinfo">
  <div class="ff-cols">
    <nav aria-label="This page"><b>This page</b><a href="#with-aura">At Aura Platform</a><a href="#law">Law</a><a href="#insurance">Insurance</a><a href="#conversation">Write to me</a></nav>
    <nav aria-label="Products"><b>Products</b><a href="{CO}/orchestrate" rel="noopener">Orchestrate ↗</a><a href="{CO}/aura" rel="noopener">Aura ↗</a><a href="{CO}/colophon" rel="noopener">Colophon ↗</a></nav>
    <nav aria-label="Company"><b>Company</b><a href="{CO}" rel="noopener">Aura Platform LLC ↗</a><a href="{CO}/films" rel="noopener">Films ↗</a><a href="{CO}/get" rel="noopener">Get the apps ↗</a></nav>
  </div>
  <small>© 2026 Iffat S. Chaudhry</small>
</footer>
<script src="record.js" defer></script>
</body>
</html>
'''
with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print('page written')
