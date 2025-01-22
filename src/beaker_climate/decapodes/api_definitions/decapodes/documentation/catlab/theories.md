


# Standard library of theories


Through the module `Catlab.Theories`, Catlab provides a standard library of [generalized algebraic theories](https://algebraicjulia.github.io/GATlab.jl) for categories, monoidal categories, and other categorical structures. The theories correspond, in most cases, to standard definitions in category theory and they are used throughout Catlab and the AlgebraicJulia ecosystem to structure programs and provide a common interface for applied category theory. The module also provides default syntax systems for many of the theories.


Categorical structures for which theories are provided include:


  * categories
  * monoidal and symmetric monoidal categories
  * cartesian and cocartesian categories
  * semiadditive categories/biproduct categories
  * hypergraph categories
  * bicategories of relations
  * categories with two monoidal products, such as distributive monoidal categories


The contents of this module can be supplemented by the user, and it is even possible to use many parts of Catlab without using this module. The user is free to create new syntax systems for the theories defined here and also to define entirely new theories.

**`Catlab.Theories`** &mdash; *Module*.



Catlab's standard library of generalized algebraic theories.

The focus is on categories and monoidal categories, but other related structures are also included.

**`Catlab.Theories.CategoryExpr`** &mdash; *Type*.



Base type for GAT expressions in categories or other categorical structures.

All symbolic expression types exported by `Catlab.Theories` are subtypes of this abstract type.

**`Catlab.Theories.HomExpr`** &mdash; *Type*.



Base type for morphism expressions in categorical structures.

**`Catlab.Theories.ObExpr`** &mdash; *Type*.



Base type for object expressions in categorical structures.

**`Base.collect`** &mdash; *Method*.



Collect generators of object in monoidal category as a vector.

**`Base.ndims`** &mdash; *Method*.



Number of "dimensions" of object in monoidal category.

