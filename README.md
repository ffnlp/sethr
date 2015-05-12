### The SETimes.HR+ Croatian dependency treebank

The treebank is a result of an effort in providing [free-culture](http://creativecommons.org/freeworks) language resources for Croatian by the [NLP group at FF Zagreb](http://nlp.ffzg.hr).

The dataset is available under the [CC-BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/). Please cite [Agić and Ljubešić (2014)](http://www.lrec-conf.org/proceedings/lrec2014/pdf/690_Paper.pdf) ([bib](http://aclweb.org/anthology/L/L14/L14-1542.bib)) when using this resource.

There are currently 6,477 sentences in the collection. All are split and tokenized, and manually annotated for:

1. parts of speech and morphological features in [Multext East v4 (MTE4)](http://nlp.ffzg.hr/data/tagging/msd-hr.html) style, and 
2. syntactic dependencies following a simplified [PDT](https://ufal.mff.cuni.cz/pdt3.0)-motivated scheme [(Agić & Merkler 2013)](http://link.springer.com/chapter/10.1007/978-3-642-40585-3_70).

On top of that, we also provide an [Universal Dependencies (UD)](http://universaldependencies.github.io/docs/) annotation layer for a large part of the treebank:

3. [universal POS tags](http://universaldependencies.github.io/docs/u/pos/all.html) with [universal morphological features](http://universaldependencies.github.io/docs/u/feat/all.html), and 
4. [UD dependency relations](http://universaldependencies.github.io/docs/u/dep/all.html).

We encode the treebank using the [CONLL-U format](http://universaldependencies.github.io/docs/format.html) from the UD project. Note that columns 4 and 5 contain the coarse- and fine-grained MTE4 tags, while column 6 splits the fine-grained MTE4 tags into the corresponding attribute-value pairs. Columns 9 and 10 capture the Universal Dependencies layer of the treebank, i.e, the head:label syntactic pairs (column 9), and the universal POS tags and morphological features as attribute-value pairs (column 10).

The treebank is split into training and test sets. The training sets are in Croatian, while the test sets are split by language (Croatian, Serbian) and domain (newswire, Wikipedia), following Agić et al. ([2013a](http://www.aclweb.org/anthology/W/W13/W13-2408.pdf), [2013b](http://www.aclweb.org/anthology/W/W13/W13-4903.pdf)).

The training sets are packaged in two files:

* `set.hr.conll` contains 3,757 training sentences (83,640 words) with both annotation layers available (SETimes.HR & UD). Note that this dataset is split in the Croatian UD dataset into 3,557 training and 200 development sentences.
* `web.hr.conll` contains 2,223 sentences (49,077 words) from the Croatian web-based corpus described by [Klubička & Ljubešić (2014)](http://nl.ijs.si/isjt14/proceedings/isjt2014_10.pdf). Currently, this dataset does not include the UD annotation layer.

The training sets are split into five 100-sentence (~2,000-word) files:

* `{set|wiki}.{hr|sr}.test.conll` are the Croatian and Serbian newswire and Wikipedia test sets, and
* `web.hr.test.conll` is the Croatian web-based test set.

For the Croatian and Serbian newswire and Wikipedia test sets, both annotation layers are available, while for the Croatian web-based test set, only the SETimes.HR annotations are currently included.

On top of these resources, we also provide the Apertium morphological lexicon of Croatian mapped to the tagset used in the above datasets (file `apertium.lexicon.2013-04-19.txt.gz`), and the tag and morphological feature mappings between MTE4 and UD (file `ttt`).
