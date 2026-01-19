# Gloss + Codex Examples v0.1

These examples are illustrative. They show Codex Concepts with `id`/`key` and Gloss annotations embedded in Codex `Content`.

For the HTML outputs below, assume a renderer that:

- defaults to emitting a `span` with semantic metadata as `data-*` attributes
- emits links as `a` when the bound Concept is a `Link` with an `href`
- emits strong emphasis as `strong` when the bound Concept is `StrongEmphasis`
- emits foreign terms as `i` with `lang` when the bound Concept is `ForeignTerm`

These HTML examples are **informative** and intentionally show one plausible mapping.

## 1. Basic Entity Reference (`@`)

```cdx
<Book id=book:hobbit key=~hobbit title="The Hobbit" author="J.R.R. Tolkien" />

<Essay id=essay:favorites>
	I love {@book:hobbit}.
	I love {@book:hobbit | The Hobbit}.
</Essay>
```

Possible HTML output:

```html
<p>
	I love <span data-gloss="@" data-cdx-id="book:hobbit">The Hobbit</span>.
	I love <span data-gloss="@" data-cdx-id="book:hobbit">The Hobbit</span>.
</p>
```

## 2. Lookup Reference (`~`) to a Non-Entity Concept

```cdx
<StrongEmphasis key=~strong />

<Note key=~n1>
	This is {~strong | important}.
</Note>
```

Possible HTML output:

```html
<p>
	This is <strong data-gloss="~" data-cdx-key="~strong">important</strong>.
</p>
```

## 3. A Quote Entity with Metadata

```cdx
<Person id=person:borges key=~borges name="Jorge Luis Borges" />
<Work id=work:tlon key=~tlon title="Tlön, Uqbar, Orbis Tertius" />
<PublicationDate key=~pubDate value="1940" />

<Quote id=quote:tlon:opening author=person:borges source=work:tlon date=~pubDate>
	I shall not attempt to justify this story.
</Quote>

<Article id=article:gloss-demo>
	Here is the opening line: {@quote:tlon:opening}.
</Article>
```

Possible HTML output:

```html
<p>
	Here is the opening line:
	<q data-gloss="@" data-cdx-id="quote:tlon:opening"
		 data-cdx-author="person:borges"
		 data-cdx-source="work:tlon"
		 data-cdx-date-key="~pubDate">
		I shall not attempt to justify this story.
	</q>.
</p>
```

## 4. Link + Foreign Term (Nested: 2 levels)

The label for a link contains a nested span for a foreign term.

```cdx
<Link key=~doc1 href="https://example.org/papers/1" />
<ForeignTerm key=~zeitgeist lang="de" translation="spirit of the age" />

<Paragraph key=~p1>
	Read {~doc1 | the discussion of {~zeitgeist | Zeitgeist}} for details.
</Paragraph>
```

Possible HTML output:

```html
<p>
	Read
	<a data-gloss="~" data-cdx-key="~doc1" href="https://example.org/papers/1">
		the discussion of <i data-gloss="~" data-cdx-key="~zeitgeist" lang="de" title="spirit of the age">Zeitgeist</i>
	</a>
	for details.
</p>
```

## 5. Link + Foreign Term + Translation (Nested: 3 levels)

A three-level nesting example:

- outer: link
- middle: foreign term
- inner: translation gloss

```cdx
<Link key=~doc2 href="https://example.org/refs/zeitgeist" />
<ForeignTerm key=~ft1 lang="de" />
<Translation key=~tr1 lang="en" />

<Paragraph key=~p2>
	See {~doc2 | {~ft1 | Zeitgeist ({~tr1 | spirit of the age})}}.
</Paragraph>
```

Possible HTML output:

```html
<p>
	See
	<a data-gloss="~" data-cdx-key="~doc2" href="https://example.org/refs/zeitgeist">
		<i data-gloss="~" data-cdx-key="~ft1" lang="de">
			Zeitgeist
			(<span data-gloss="~" data-cdx-key="~tr1" lang="en">spirit of the age</span>)
		</i>
	</a>.
</p>
```

## 6. Mixed `@` and `~` with Multiple Spans

```cdx
<Person id=person:camus key=~camus name="Albert Camus" />
<Work id=work:myth key=~sisyphus title="The Myth of Sisyphus" />
<Link key=~external href="https://example.org/camus" />

<Paragraph id=para:camus>
	{@person:camus | Camus} discusses {~sisyphus | this work}. 
	External reference: {~external | author bio}.
</Paragraph>
```

Possible HTML output:

```html
<p>
	<span data-gloss="@" data-cdx-id="person:camus">Camus</span> discusses
	<span data-gloss="~" data-cdx-key="~sisyphus">this work</span>.
	External reference:
	<a data-gloss="~" data-cdx-key="~external" href="https://example.org/camus">author bio</a>.
</p>
```
