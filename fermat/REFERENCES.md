# Verified Mathematical Bibliography & References

This document provides a verified, annotated bibliography of the original mathematical literature and recent formal verification breakthroughs cited in [`fermat_proof.tex`](file:///Users/eric/Dropbox/ai/fermat/fermat_proof.tex).

Every paper listed below is genuine, published in recognized peer-reviewed mathematics journals or authoritative institutional archives.

---

## 1. The Core 1995 Wiles Papers (The Modularity Theorem)

### [1] Wiles, Andrew (1995)
* **Title:** *Modular elliptic curves and Fermat's Last Theorem*
* **Journal:** *Annals of Mathematics*, Second Series, Vol. 141, No. 3 (May, 1995), pp. 443–551.
* **DOI:** [10.2307/2118559](https://doi.org/10.2307/2118559)
* **JSTOR:** [jstor.org/stable/2118559](https://www.jstor.org/stable/2118559)
* **Role in Proof:** The foundational paper proving the semistable case of the Taniyama-Shimura-Weil conjecture (the Modularity Theorem). Introduced the $R = T$ strategy connecting deformation rings of Galois representations to Hecke algebras.

### [2] Taylor, Richard & Wiles, Andrew (1995)
* **Title:** *Ring-theoretic properties of certain Hecke algebras*
* **Journal:** *Annals of Mathematics*, Second Series, Vol. 141, No. 3 (May, 1995), pp. 553–572.
* **DOI:** [10.2307/2118560](https://doi.org/10.2307/2118560)
* **JSTOR:** [jstor.org/stable/2118560](https://www.jstor.org/stable/2118560)
* **Role in Proof:** Resolved the critical gap in Wiles' original 1993 argument. Introduced "Taylor-Wiles systems" of auxiliary primes to prove that the Hecke ring $T$ is a complete intersection and isomorphic to the deformation ring $R$.

---

## 2. Level-Lowering & Serre's Conjectures

### [3] Ribet, Kenneth A. (1990)
* **Title:** *On modular representations of $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ arising from modular forms*
* **Journal:** *Inventiones Mathematicae*, Vol. 100, Issue 1, pp. 431–476.
* **DOI:** [10.1007/BF01231195](https://doi.org/10.1007/BF01231195)
* **Role in Proof:** Proved Serre's $\varepsilon$-conjecture ("level-lowering"). Proved that if an elliptic curve is modular and its mod $p$ representation is unramified at a prime dividing the conductor, the modular form can be lowered to a level where that prime is removed.

### [4] Serre, Jean-Pierre (1987)
* **Title:** *Sur les représentations modulaires de degré 2 de $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$*
* **Journal:** *Duke Mathematical Journal*, Vol. 54, No. 1, pp. 179–230.
* **DOI:** [10.1215/S0012-7094-87-05413-5](https://doi.org/10.1215/S0012-7094-87-05413-5)
* **Role in Proof:** Formulated the definitive conjectures (including the $\varepsilon$-conjecture) relating odd, irreducible, two-dimensional mod $p$ representations of $G_\Q$ to modular forms of specific weight and minimal conductor.

---

## 3. The Frey Curve & Torsion Obstructions

### [5] Frey, Gerhard (1986)
* **Title:** *Links between stable elliptic curves and certain Diophantine equations*
* **Journal:** *Annales Universitatis Saraviensis. Series Mathematicae*, Vol. 1, No. 1, pp. 1–40.
* **ISSN:** 0933-5846
* **Role in Proof:** First constructed the curve $y^2 = x(x - a^p)(x + b^p)$ associated with a hypothetical Fermat solution and conjectured that its minimal discriminant $\Delta = 2^{-8}(abc)^{2p}$ was so unusual that the curve could not be modular.

### [6] Mazur, Barry (1977)
* **Title:** *Modular curves and the Eisenstein ideal*
* **Journal:** *Publications Mathématiques de l'IHÉS*, Vol. 47, pp. 33–186.
* **NUMDAM:** [numdam.org/item/PMIHES_1977__47__33_0](http://www.numdam.org/item/PMIHES_1977__47__33_0/)
* **Role in Proof:** Classified all possible rational torsion points on elliptic curves over $\mathbb{Q}$. Proved that semistable elliptic curves have no rational subgroups of prime order $p \ge 5$, directly guaranteeing the irreducibility of $\bar{\rho}_{E,p}$.

---

## 4. Authoritative Textbooks & Expositions

### [7] Darmon, Henri; Diamond, Fred; & Taylor, Richard (1997)
* **Title:** *Fermat's Last Theorem*
* **Book:** *Elliptic Curves, Modular Forms and Fermat's Last Theorem*, edited by J. Coates and S. T. Yau.
* **Publisher:** International Press, Cambridge, MA, pp. 2–140.
* **Preprint / PDF:** [McGill University Faculty Archive](https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf)
* **Role in Proof:** The definitive pedagogical exposition simplifying Wiles' proof, which serves as the blueprint for modern presentations and formalizations.

### [8] Silverman, Joseph H. (2009)
* **Title:** *The Arithmetic of Elliptic Curves*
* **Series:** *Graduate Texts in Mathematics*, Vol. 106.
* **Publisher:** Springer, New York, 2nd edition.
* **ISBN:** 978-0-387-09493-9
* **DOI:** [10.1007/978-0-387-09494-6](https://doi.org/10.1007/978-0-387-09494-6)
* **Role in Proof:** Standard reference for minimal Weierstrass models, Tate's algorithm for conductor calculations, and the theory of the Tate curve at non-archimedean places.

### [9] Diamond, Fred & Shurman, Jerry (2005)
* **Title:** *A First Course in Modular Forms*
* **Series:** *Graduate Texts in Mathematics*, Vol. 228.
* **Publisher:** Springer, New York.
* **ISBN:** 978-0-387-23229-4
* **DOI:** [10.1007/978-0-387-27226-9](https://doi.org/10.1007/978-0-387-27226-9)
* **Role in Proof:** Standard reference for the dimension formulas of spaces of cusp forms $S_k(\Gamma_0(N))$, proving that $\dim S_2(\Gamma_0(2)) = g(X_0(2)) = 0$.

---

## 5. Machine Verification & Autoformalization (2026)

### [10] Anthropic & Peng, Tianyi et al. (2026)
* **Title:** *Formalizing Fermat's Last Theorem*
* **Outlet:** *Anthropic Research*, Published September 4, 2026.
* **URL:** [anthropic.com/research/formalizing-fermats-last-theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
* **Code Repository:** [github.com/anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem)
* **Role:** The first complete, end-to-end, computer-checked proof of Fermat's Last Theorem in Lean 4, written by multi-agent Claude models over 11 days (13 million lines of Lean code, 29,500 intermediate theorems).

### [11] Chen, Shuze; Marwaha, Kunal; Lu, Xiaoyang; Yuen, Henry; & Peng, Tianyi (2026)
* **Title:** *Prove2Me: An Open Collaborative Platform for Scaling Math Formalization*
* **Archive:** arXiv preprint, arXiv:2608.28433 [cs.AI, math.LO].
* **arXiv URL:** [arxiv.org/abs/2608.28433](https://arxiv.org/abs/2608.28433)
* **Platform:** [prove2.me](https://prove2.me)
* **Role:** Introduced the open collaborative DAG harness and proof decomposition platform that enabled multi-agent systems to collaborate without context rot, forming the scaffold used for the FLT formalization.
