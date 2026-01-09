# Jimmy Example

## The "Say What You Mean" article

```cdx
<Article id="article:_XZeUccqMWb82LGCY8u8v64" kind="think">
  <Title>Say What You Mean: How Fancy Words Make You Sound Anything But!</Title>

  <ReadingTime id="readingTime" value={PT12M} />
  <PublishedOn id="publishedOn" value=2025-07-28 />
  <Tag id="tag:analysis" name="analysis" />

  <HeroImage id="hero:words">
    <ImageSource format="avif" uri="https://ik.imagekit.io/jbdhtp3sm/jimmyco/tr:f-avif/thinks/words-words-words.png" />
    <ImageSource format="webp" uri="https://ik.imagekit.io/jbdhtp3sm/jimmyco/tr:f-webp/thinks/words-words-words.png" />
    <ImageSource uri="https://ik.imagekit.io/jbdhtp3sm/jimmyco/thinks/words-words-words.png" />
    <AltText>Black and white illustration of a woman's mouth and lips with a speech bubble filled with repeated text reading "WORDS WORDS WORDS".</AltText>
  </HeroImage>

  <Paragraph>
    {#important | Our workplaces have some truly bonkers vocab}.
    We've slapped the most ridiculous professional labels on things.
    {#quotation | Document analysis?} That's {#stress | reading}.
    {#quotation | Requirements elicitation?} That's asking people what they need.
    {#quotation | Gap analysis?} That's working out what's missing.
  </Paragraph>

  <Paragraph>
    We've managed to make the simplest activities sound like they require advanced degrees
    and certification programs. Anything to make a buck I guess?
  </Paragraph>

  <Paragraph>
    Take {#quotation | stakeholder management,} for example …
  </Paragraph>

  <Section id="sec:stakeholderManagement">
    <Heading>Stakeholder management!</Heading>

    <Work id="work:buffy" title="Buffy the Vampire Slayer" />
    <Link id="link:buffyWiki" uri="https://en.wikipedia.org/wiki/Buffy_the_Vampire_Slayer" rel="external" />

    <Paragraph>
      For some reason the phrase {#quotation | stakeholder} reminds me of a line in
      {@work:buffy | Buffy the Vampire Slayer}.
      In the scene Spike is explaining his intentions to Buffy, {#emphasis | claiming}
      he doesn't have romantic ideals of them shacking up in a little house with a white picket fence.
    </Paragraph>

    <Paragraph>
      He remarks (about the white picket fence), that it is
      {#quotation | bloody dangerous for one thing}.
    </Paragraph>

    <Paragraph>
      Amusingly, the concept that stakeholders are {#emphasis | literally dangerous}
      isn't entirely without merit. They might not be holding literal stakes,
      but they can stab you just the same.
    </Paragraph>

    <Paragraph>
      Case in point: I spent the vast majority of my career believing that
      {#quotation | document analysis} was some fancy research technique.
      Turns out it just means {#quotation | to look at carefully at documents so as to understand the meaning of}.
    </Paragraph>

    <Paragraph>
      In case this doesn't seem familiar, {#important | this is literally the definition of reading}.
      Yup! We put a fancy label on {#stress | reading}. We obscure it. Jazz it up.
      We never just say what we mean.
    </Paragraph>

    <Paragraph>
      This is the definition of {#jargon | jargon}.
    </Paragraph>
  </Section>

  <Section id="sec:jargon">
    <Heading>Jargon.</Heading>

    <Paragraph>
      {#definition | Jargon} is specialised or technical language that is not understood
      outside of a specific group.
    </Paragraph>

    <Paragraph>
      Don't get me wrong, {#important | jargon serves a purpose} and amongst experts it can be an easy shorthand.
      But it also signals club membership, creates insider knowledge, and pushes the cognitive cost onto the reader.
    </Paragraph>
  </Section>

  <Section id="sec:coolWords">
    <Heading>Because some words are just extremely excellent and demand to be used</Heading>

    <OrderedList>
      <ListItem>{#highlight | Instantiate}.</ListItem>
      <ListItem>{#highlight | Fractal}.</ListItem>
      <ListItem>{#highlight | Penultimate}.</ListItem>
    </OrderedList>

    <Paragraph>
      I remain convinced that in all other situations, lingo is not the answer.
      (Note: I cannot resist pointing out that this is the {#wordAsWord | penultimate} paragraph of this article — you're welcome).
    </Paragraph>
  </Section>

  <LastUpdated id="lastUpdated" value=2025-07-28 />
</Article>
```

## The ViewModel

The ViewModel is a pure, target-neutral Codex structure shaped by Scribe from queried semantic data.
It represents what exists structurally, with all meaning resolved but no presentation decisions applied.

```json
{
  "type": "ArticleViewModel",
  "id": "article:_XZeUccqMWb82LGCY8u8v64",
  "title": "Say What You Mean: How Fancy Words Make You Sound Anything But!",
  "readingTime": { "minutes": 12 },
  "dates": {
    "publishedOn": "2025-07-28",
    "lastUpdated": "2025-07-28"
  },
  "tags": ["analysis"],
  "hero": {
    "type": "Image",
    "sources": [
      { "uri": "https://ik.imagekit.io/jbdhtp3sm/jimmyco/tr:f-avif/thinks/words-words-words.png", "format": "avif" },
      { "uri": "https://ik.imagekit.io/jbdhtp3sm/jimmyco/tr:f-webp/thinks/words-words-words.png", "format": "webp" },
      { "uri": "https://ik.imagekit.io/jbdhtp3sm/jimmyco/thinks/words-words-words.png", "format": "png" }
    ],
    "altText": "Black and white illustration of a woman's mouth and lips with a speech bubble filled with repeated text reading WORDS WORDS WORDS."
  },
  "sections": [
    {
      "id": "intro",
      "heading": null,
      "blocks": [
        {
          "type": "Paragraph",
          "spans": [
            { "text": "Our workplaces have some truly bonkers vocab", "gloss": [{ "kind": "NonEntityRef", "ref": "important" }] },
            { "text": ". We've slapped the most ridiculous professional labels on things. " },
            { "text": "Document analysis", "gloss": [{ "kind": "NonEntityRef", "ref": "quotation" }] },
            { "text": "? That's " },
            { "text": "reading", "gloss": [{ "kind": "NonEntityRef", "ref": "stress" }] },
            { "text": ". " },
            { "text": "Requirements elicitation", "gloss": [{ "kind": "NonEntityRef", "ref": "quotation" }] },
            { "text": "? That's asking people what they need. " },
            { "text": "Gap analysis", "gloss": [{ "kind": "NonEntityRef", "ref": "quotation" }] },
            { "text": "? That's working out what's missing." }
          ]
        }
      ]
    },
    {
      "id": "sec:stakeholderManagement",
      "heading": { "text": "Stakeholder management!" },
      "blocks": [
        {
          "type": "Paragraph",
          "spans": [
            { "text": "For some reason the phrase " },
            { "text": "stakeholder", "gloss": [{ "kind": "NonEntityRef", "ref": "quotation" }] },
            { "text": " reminds me of a line in " },
            { "text": "Buffy the Vampire Slayer", "gloss": [{ "kind": "EntityRef", "ref": "work:buffy", "labelOverride": null }] },
            { "text": "." }
          ],
          "entityMentions": [{ "entityId": "work:buffy" }]
        }
      ],
      "entities": [
        {
          "id": "work:buffy",
          "type": "Work",
          "title": "Buffy the Vampire Slayer",
          "sameAs": "https://en.wikipedia.org/wiki/Buffy_the_Vampire_Slayer"
        }
      ]
    }
  ],
  "glossResolution": {
    "resolvedNonEntityRefs": ["important", "quotation", "stress"],
    "unresolvedRefs": []
  },
  "helps": []
}
```

# The DesignPolicy

The Design Policy is authored by humans in CDX and expresses presentation intent declaratively.
It says how meaning should be realized for a class of targets, without changing semantics or structure.

```cdx
<DesignPolicy id="policy:article:default" targetClass="screen" locale="en-NZ">
  [This policy applies to Article ViewModels.]
  <AppliesTo concept="Article" />

  [Inline semantics: Quotation becomes a quote span; quote marks are locale-owned.]
  <InlineRealization for="Quotation">
    <Html element="q" />
    <LocaleQuotes>
      <Quotes locale="en-NZ" open="“" close="”" />
      <Quotes locale="en-US" open="“" close="”" />
      <Quotes locale="en-GB" open="‘" close="’" />
    </LocaleQuotes>
    <Audio prosody="quoted" />
  </InlineRealization>

  [Inline semantics: Stress becomes emphasis.]
  <InlineRealization for="Stress">
    <Html element="em" class="stress" />
    <Audio prosody="emphasis" />
  </InlineRealization>

  [Inline semantics: Important becomes strong emphasis.]
  <InlineRealization for="Important">
    <Html element="strong" class="important" />
    <Audio prosody="strong" />
  </InlineRealization>

  [Entity references: linking is a policy decision, not Gloss syntax.]
  <EntityReferencePolicy defaultLinking="conditional">
    [If an Entity has a sameAs trait, link to it; otherwise do not link.]
    <LinkWhen hasTrait="sameAs">
      <Html linkToTrait="sameAs" rel="external" />
    </LinkWhen>
    <Otherwise>
      <Html noLink=true />
    </Otherwise>
  </EntityReferencePolicy>

  [Metadata emission: for HTML-class targets, default to JSON-LD.]
  <MetadataPolicy>
    <Html emit="jsonld" when="entitiesReferenced" />
  </MetadataPolicy>

  [Block mapping for common ViewModel blocks.]
  <BlockRealization for="Paragraph" htmlElement="p" />
  <BlockRealization for="Section" htmlElement="section" />
  <BlockRealization for="Heading" htmlElement="h2" />
</DesignPolicy>
```

# The Presentation Plan

The Presentation Plan is a Codex artifact generated by Scribe by applying Design Policy to a ViewModel.

It is a human-readable, deterministic plan describing what will be rendered, step by step, without executing anything.

```cdx
<PresentationPlan id="plan:article:_XZeUccqMWb82LGCY8u8v64:screen:html" target="html" targetClass="screen" locale="en-NZ">
  [This plan was produced by applying a DesignPolicy to a specific ViewModel.]
  <PlanFor viewModelId="article:_XZeUccqMWb82LGCY8u8v64" designPolicyId="policy:article:default" />

  [Render the outer article container and header metadata.]
  <RenderArticleShell />
  <RenderHeader>
    <Include field="title" />
    <Include field="readingTime" />
    <Include field="publishedOn" />
    <Include field="tags" />
  </RenderHeader>

  [Render hero media if present.]
  <RenderHeroImage />

  [Render document sections and blocks in order.]
  <RenderSections>
    <RenderBlock kind="Heading" htmlElement="h2" />
    <RenderBlock kind="Paragraph" htmlElement="p" />
    <RenderBlock kind="Section" htmlElement="section" />
    <RenderBlock kind="OrderedList" htmlElement="ol" />
    <RenderBlock kind="UnorderedList" htmlElement="ul" />
    <RenderBlock kind="ListItem" htmlElement="li" />
  </RenderSections>

  [Apply inline realizations produced from Gloss semantics.]
  <ApplyInlineRealizations>
    [Quotation realization uses locale-owned quotes and/or HTML <q> behavior.]
    <Inline for="Quotation" htmlElement="q" quoteStyle="locale" />
    <Inline for="Stress" htmlElement="em" class="stress" />
    <Inline for="Important" htmlElement="strong" class="important" />
  </ApplyInlineRealizations>

  [Resolve Entity references into link actions per policy.]
  <ApplyEntityReferencePolicy>
    <LinkWhen hasTrait="sameAs" linkToTrait="sameAs" rel="external" />
    <OtherwiseNoLink />
  </ApplyEntityReferencePolicy>

  [Emit metadata for referenced Entities using the default HTML strategy.]
  <EmitMetadata format="jsonld" when="entitiesReferenced" />

  [Render footer metadata if present.]
  <RenderFooter>
    <Include field="lastUpdated" />
  </RenderFooter>
</PresentationPlan>
```

## The HTML Output

The HTML output is produced by executing the Presentation Plan for a specific render target.
It is one possible realization of the plan, not the source of truth.

```html
<article data-article-id="article:_XZeUccqMWb82LGCY8u8v64">
  <header class="think-header">
    <h1>Say What You Mean: How Fancy Words Make You Sound Anything But!</h1>

    <div class="time-to-read-and-date">
      <div class="time-to-read">12 min read</div>
      <time class="published-on" datetime="2025-07-28">28 July 2025</time>
    </div>

    <ul class="page-tags">
      <li class="page-tag">analysis</li>
    </ul>

    <figure class="hero-img">
      <picture aria-labelledby="hero-caption">
        <source srcset="https://ik.imagekit.io/jbdhtp3sm/jimmyco/tr:f-avif/thinks/words-words-words.png" type="image/avif" />
        <source srcset="https://ik.imagekit.io/jbdhtp3sm/jimmyco/tr:f-webp/thinks/words-words-words.png" type="image/webp" />
        <img
          src="https://ik.imagekit.io/jbdhtp3sm/jimmyco/thinks/words-words-words.png"
          alt=""
          width="1000"
          height="563"
          loading="eager"
          decoding="auto"
        />
      </picture>

      <div class="sr-only" id="hero-caption">
        <p>
          Black and white illustration of a woman's mouth and lips with a speech bubble filled with
          repeated text reading 'WORDS WORDS WORDS
        </p>
      </div>
    </figure>

    <p>
      <strong class="important">Our workplaces have some truly bonkers vocab</strong>. We've slapped
      the most ridiculous professional labels on things. <q>Document analysis</q>? That's
      <em class="stress">reading</em>. <q>Requirements elicitation</q>? That's asking people what
      they need. <q>Gap analysis</q>? That's working out what's missing.
    </p>

    <p>
      We've managed to make the simplest activities sound like they require advanced degrees and
      certification programs. Anything to make a buck I guess?
    </p>

    <p>
      It's as if we collectively decided that sounding important was more valuable than being
      understood. Which would be merely amusing if it wasn't so counterproductive.
    </p>

    <p>Take <q>stakeholder management,</q> for example …</p>
  </header>

  <section id="stakeholder-management">
    <header>
      <h2>Stakeholder management!</h2>
    </header>

    <p>
      For some reason the phrase <q>stakeholder</q> reminds me of a particular line in one of the
      later seasons of
      <a href="https://en.wikipedia.org/wiki/Buffy_the_Vampire_Slayer" rel="external"
        >Buffy the Vampire Slayer</a
      >. In the scene Spike is explaining his intentions to Buffy, <em>claiming</em> that he
      doesn't have romantic ideals of them shacking up in a little house with a white picket fence.
    </p>

    <p>
      He remarks (about the white picket fence), that it is <q>bloody dangerous for one thing</q>.
    </p>

    <p>
      Now, in case you aren't a millennial of the female variety I'll explain why this is funny:
      Spike is a vampire and a white picket fence is basically a row of stakes. He's right, 'tis
      bloody dangerous in the context. (Also note: I couldn't find a clip of this scene so you're
      running on Hannah's memory alone for this which is also dangerous).
    </p>

    <p>
      I know, neither Spike or Buffy mention stakeholders. But in my brain the word
      <q>stakeholder</q> and this scene are irreparably and intrinsically linked. When someone says
      <q>stakeholder</q> I conjure images of people literally holding sharp sticks. Then my brain
      jumps to vampires, then to this scene (lol!), and then eventually my brain makes its way back
      to the topic at hand: actual real world stakeholders.
    </p>

    <p>
      Amusingly, the concept that stakeholders are <em>literally dangerous</em> isn't entirely
      without merit. Your stakeholders might not be holding literal stakes, but they can stab you
      just the same. Spike is onto something: dealing with stake(holder)s is bloody dangerous work.
    </p>

    <p>
      It's also funny to me that our civilised and professional term for wrangling people is kind of
      on the money?
    </p>

    <p>A fact that makes it pretty unique.</p>

    <p>
      Case in point: I spent the vast majority of my career believing that
      <q>document analysis</q> was some fancy research technique. Turns out it just means
      <q>to look at carefully at documents so as to understand the meaning of</q>.
    </p>

    <p>In case this doesn't seem familiar, <strong>this is literally the definition of reading</strong>.</p>

    <p>
      Yup! We put a fancy label on <em>reading</em>. We obscure it. Jazz it up. Make it sound
      important. Maybe you need certification to undertake such a laborious and intensive task? We
      never just say what we mean.
    </p>

    <p>This is the definition of jargon.</p>
  </section>

  <section id="pattern">
    <header>
      <h2>It's a pattern</h2>
    </header>

    <p>
      Doesn't every functioning adult do <q>gap analysis</q> every time they look in their fridge and
      cupboard before heading to the grocery store? We all do <q>root cause analysis</q> when we
      encounter a problem — flat tire? Was it a nail or sabotage? Likely the most dangerous form of
      <q>stakeholder management</q> is keeping your mother in law happy during a holiday meal. And
      aren't we doing <q>requirements elicitation</q> when we gather everyone's preferences and
      constraints before we order takeaways?
    </p>

    <p>
      The difference is we'd <em>never</em> use those terms in those settings. At work, though? We
      take these same normal human activities — reading, asking questions, keeping track of things —
      and wrap them in professional language that makes them sound way more complicated than they
      really are.
    </p>

    <p>
      This attachment to jargon — where we dress up what we do — is everywhere in business analysis.
    </p>
  </section>

  <section id="jargon">
    <header>
      <h2>Jargon.</h2>
    </header>

    <p>Jargon is specialised or technical language that is not understood outside of a specific group.</p>

    <p>
      Don't get me wrong, <strong>jargon serves a purpose</strong> and amongst experts it can be an
      easy shorthand. But it has other impacts: using jargon signals that you're part of the club.
      It creates an artificial barrier between those who <q>know the lingo</q> and those who don't.
      When you casually drop terms like <q>requirements elicitation</q>and
      <q>stakeholder mapping,</q> you're not just describing activities — you're demonstrating your
      expertise and status to other members of the club.
    </p>

    <p>
      It is an elaborate inside joke. <strong>And one not without downsides</strong>.
    </p>

    <p>
      All that fancy language actually works against us. Studies show that jargon reduces the actual
      understanding of the message, reduces the perceived clarity, and also reduces the recipient's
      confidence in the accuracy of the message. Most importantly, there's evidence to suggest that
      too much jargon undermines trust and credibility in the speaker. In our roles — where our
      position is entirely based on trust and often on our personal credibility — you can see that
      this is a bit of a problem, no?
    </p>

    <p>
      And this is all without even mentioning the impact on collaboration and team work: creating
      <q>insider</q> knowledge is inherently exclusionary to anyone not familiar with the jargon
      (this is <em>especially</em> true for anyone who is operating in a language which is not their
      native tongue). People unfamiliar with the terms have to interrupt the flow to clarify — an
      act that requires a certain level of confidence that not everyone has in spades.
    </p>

    <p>Deciphering nonsense takes effort and time that is in short supply.</p>

    <p>
      <strong
        >Ironically, research has also found that clear, straightforward language generally makes
        the speaker sound more credible</strong
      >. And when people aren't overloaded with buzzwords and jargon they have more mental capacity
      to spend on the actual message.
    </p>

    <p>A finding that absolutely aligns with my experience in the wild.</p>

    <p>
      Stakeholders feel lost and confused and bewildered if you use jargon. Our managers don't
      understand what (or why) we're doing anything when we hide behind buzzwords. And our
      colleagues suspect we're taking the piss (they're not entirely wrong).
    </p>

    <p>
      The only people who you impress with your jargon is other experts and there are limited
      situations when other experts really matter to your success.
    </p>

    <p>When you're not kicking around on LinkedIn that is.</p>
  </section>

  <section id="better-way">
    <header>
      <h2>There is a better way</h2>
    </header>

    <p>Okay, so fine, jargon sucks. We shouldn't use it. It bad.</p>

    <p>But can you actually ditch the jargon and still sound like you know what you're doing?</p>

    <p>
      Well, it can feel scary — at least at first. And especially scary if you have been told that
      the lingo matters. When you say <q>I read through the documents and talked to people to figure out what they needed,</q>
      instead of <q>I conducted stakeholder analysis and requirements elicitation,</q> there's this
      moment where you think you sound daft. Like you're not actually being helpful. Like you're
      just doing really obvious simple stuff that doesn't move the work forward.
      <em>Like what are you even doing in this room?</em>
    </p>

    <p>But keeping things simple is the very essence of expertise in action.</p>

    <p>
      True expertise isn't in any one particular skill or activity. It is far more about knowing
      <em>which</em> documents to read, <em>who</em> to talk to, <em>how</em> to make sense of what
      you find, and <em>what</em> skill to apply. It's seeing the patterns, asking the right follow-up
      questions, and connecting dots that other people miss. When you can easily <em>and simply</em>
      explain what you actually did and how it helped — that's when people really start to trust
      that you know your stuff.
    </p>

    <p>
      So instead of <q>stakeholder management,</q> maybe say <q>keeping everyone in the loop and making sure they continue to support us.</q>
      Instead of <q>gap analysis,</q> you could say <q>figuring out what's missing.</q>
      Instead of <q>requirements elicitation,</q> perhaps say <q>working out what people actually need (which will inevitably be different from what they say they want).</q>
    </p>

    <p>
      When we talk about our work in plain language, people actually understand what we do. And
      remarkably, they usually have brains and eyes and they can see how it helps the bigger
      picture.
    </p>

    <p>
      Yes, it means standing in the discomfort of sounding <q>less professional</q>. But that
      discomfort is worth it when you realise that people actually understand what you're saying.
    </p>

    <p>Trust me. You should try it.</p>
  </section>

  <section id="jargon-does-not-come-first">
    <header>
      <h2>No, jargon doesn't come first</h2>
    </header>

    <p>
      Which (finally) brings us to why I've spent my Saturday writing this spiel. Like many things,
      it was a LinkedIn post that triggered the thought. Someone was posting advice about how to
      break into business analysis, and the post claimed that <q>Language signals expertise</q> (a
      true, if somewhat misleading statement — see above), followed by
      <q><strong>if you learn the lingo, you’ll learn everything else</strong></q>
    </p>

    <p>
      Well heck. While it is possible there are other statements I disagree with more, nothing comes
      to mind.
    </p>

    <p>
      Ironically, I actually consider it my job — our job as experts — to look past lingo to the
      skills and thinking patterns that lie underneath. I couldn't care less what you call it, I
      want to know if you can see second-order impacts, if you care about people, and how you
      communicate. This is what would signal capability and expertise to me. Not the jargon you
      layered on top.
    </p>

    <p>
      Also, if you come at me with lingo, but without the actual skills, or you can talk about
      concepts, but not the realities of that activity on the ground, then I — and any other expert —
      will absolutely see through it. And if you try to hide the lack of expertise with jargon and
      lingo, the fact that you tried to hide it will seriously reduce any credibility that you had.
    </p>

    <p><strong>Lingo is actually the complete opposite of what I'm looking for.</strong></p>

    <p>
      But obviously, I'm not necessarily who is interviewing you. There are three situations where
      you should absolutely ignore my advice thus far.
    </p>

    <section id="non-experts">
      <header>
        <h3>Non-experts</h3>
      </header>

      <p>
        We all know that keyword matching is a thing that happens during recruitment, which totally
        makes sense when you think about it — recruiters usually aren't experts in the field they are
        recruiting in so have to rely on picking up on specific words that you say as a proxy for
        the expertise they're looking for.
      </p>

      <p>
        In which case, by all means make sure you hit the buzzwords when you're explaining what you
        did in your last role. And of course drop some sweet <q>stakeholder management skillz</q> on
        your CV, talk about your <q>extensive requirements elicitation experience</q>, and toot about
        your <q>ability to navigate ambiguity during large scale digital transformation programmes.</q>
      </p>

      <p>And good luck with finding a role that you love!</p>
    </section>

    <section id="those-places">
      <header>
        <h3><q>Those</q> places</h3>
      </header>

      <p>
        There is also a bunch of places where lingo does matter. Where being part of the club is
        key. Now I actively avoid working at those places so this isn't an area I know a lot about,
        but I know they do exist.
      </p>

      <p>If you want to work in such a place, then yes, you should absolutely focus on learning the lingo.</p>
    </section>

    <section id="excellent-words">
      <header>
        <h3>Because some words are just extremely excellent and demand to be used</h3>
      </header>

      <p>Sometimes words are just very cool and you should use them. The highest offenders on my buzzwordy / jargon list?</p>

      <ol>
        <li>
          <strong>Instantiate</strong>. Ever since my tech lead lectured me about the meaning of instantiate when I was a junior BA, I was in love! It was the very first concept that captured the magic of tech/digital products to me and I can't seem to stop myself using it!
        </li>
        <li>
          <strong>Fractal</strong>. Oof. When fractal is the right word there's no other word.
        </li>
        <li>
          <strong>Penultimate</strong>. OH EM GEE SUCH A GOOD WORD. I try to never miss an opportunity to use it. Saturday? That's the penultimate day of the week! 30th of December? The penultimate day of the year. I'm honestly seriously sad when I realise I have missed the opportunity to use it.
        </li>
      </ol>

      <p>
        <strong>I remain convinced that in all other situations, lingo is not the answer.</strong>
        (Note: I cannot resist pointing out that this is the penultimate paragraph of this article — you're welcome).
      </p>

      <p>So go forth and de-jargon.</p>
    </section>
  </section>

  <p class="last-updated">
    Last updated <time class="last-updated" datetime="2025-07-28" itemprop="modifiedOn">28 July 2025</time>.
  </p>

  <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "CreativeWork",
          "name": "Buffy the Vampire Slayer",
          "sameAs": "https://en.wikipedia.org/wiki/Buffy_the_Vampire_Slayer"
        }
      ]
    }
  </script>
</article>
```

## The pipeline

Codex data → ViewModel (structure) → Design Policy (intent) → Presentation Plan (decision) → HTML (realization)

- No semantics are added after Codex.
- No presentation leaks backward.
- No policy is implicit.
