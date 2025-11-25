Here are the questions that I am currently trying to answer:

- What counts as "different kinds of information" in a memory model (association, content, context, and everything)?
    
- Is it necessary to define content? How do we formally distinguish core contents (properties of the item itself, I call it core content because every model must at least say this is content) from relational or, say, 'contextual' information (this could contain massive amounts of information in different kinds here, needs more discussion)?
    
- In encoding and retrieval, what mathematically separates global-matching-based familiarity from recall-like retrieval?
    
- When does adding information require creating a new representational space, and when is it just a metric deformation of the existing one?
    
- How can different theoretical assumptions about memory be formally represented—such as memory as a tensor-product of content and context (e.g., positional or association-matrix models like Burgess & Hitch or Henson’s Start-End Model), memory as an embedding where context is expressed through metric deformation (e.g., SIMPLE), or memory as a joint item–context embedding (e.g., TCM)?
    

This is the domain I'm thinking about:

Primarily the encoding and retrieval parts of the memory cycle (not yet maintenance and forgetting), especially the boundary between global matching (SDT-based models) and recollection-style retrieval, different item context association patterns, and how these differences can be expressed firstly in measurement , then process level.

A brief summary of the line of framework I got on top of the defnition I got from last time:

I'm trying to build a measure level account that starts from the definition of different kinds of information (these contain all kinds of combinations between content and context).

My current storyline is:

Begin with an "original sample space."

This is the space where items are just basic units presented in an experiment. The samples themselves represent the _core item information_ (the minimal set of features required to identify an item as that item); THEN, any other structure carried by the measure (similarity, distance, etc.) corresponds to _relational information_ carrying different internal relationship between different information (this contains all kinds of information).

Encoding maps this original space into a psychological representational space.

Some time during encoding (before, during, after), measurement transformation is required for later use of retrieval on similarity calculation. Two independent choices arise during encoding:

- Two ways of using the core item info (the sample units) –  it could be expanded into its own feature space or not (and thus how it has the different relationships with ‘context’.) Recollection requires representational expansion relative to the original item identity. Familiarity does not necessarily require expansion. 
    
- Two ways of using the relational information – pull out the structure as a new dimension like positional coding vs. preserve the structure and use structure itself to tell discriminability (global matching model). I think one main difference between recollection/position-coding models and global matching/familiarity models is if some explicit context cue is defined and used. 
    

Different operations last step also give rise to recollection vs. familiarity:

Recall. Event-trace recall = the item representation has been expanded into a richer space. Knowledge-trace recall = the item is bound to an additional context space (e.g., position).

Familiarity. Describes relationships through the internal structure of the original space rather than through added dimensions. This aligns with global-matching and SDT-style models, where relational information is expressed as discriminability rather than explicit encoding.

Thus, the core question becomes:

When does the system stay inside the original measure (familiarity), what are the different transformations between the spaces, and when does it create or use a new measure space (recall)? (this assumption itself needs more thinking). This distinction seems to align naturally with the operator view.

Where I think I need mathematical theorems:

- A theorem distinguishing "expanding the sample" vs. "adding a new space." (Feature-space expansion vs. product-space augmentation.)
    
- A theorem characterizing when relational information can be represented by a metric deformation, and when it requires a new measurable dimension. (Embedding vs. product space.)
    
- A theorem linking global matching to the structure of the original measure. (Familiarity operates entirely within the initial internal relationship.)
    
- A theorem showing when recall emerges as a different operator order or as a higher-resolution context mapping.