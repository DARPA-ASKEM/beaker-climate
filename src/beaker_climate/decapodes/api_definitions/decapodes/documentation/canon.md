


# Canon






## Physics

**`Decapodes.Canon.Physics.:heat_transfer`** &mdash; *Constant*.



**Heat Transfer**

[Source](https://www.google.com)

**Model**

```
(HT, Tₛ)::Form0
              
(D, cosϕᵖ, cosϕᵈ)::Constant
              
HT == (D ./ cosϕᵖ) .* (⋆)(d(cosϕᵈ .* (⋆)(d(Tₛ))))
```

**`Decapodes.Canon.Physics.:outgoing_longwave_radiation`** &mdash; *Constant*.



**Outgoing Longwave Radiation**

[Source](https://www.google.com)

**Model**

```
(Tₛ, OLR)::Form0
              
(A, B)::Constant
              
OLR == A .+ B .* Tₛ
```

**`Decapodes.Canon.Physics.absorbed_shortwave_radiation`** &mdash; *Constant*.



**Absorbed Shortwave Radiation**

[Source](https://www.google.com)

The proportion of light reflected by a surface is the **albedo**. The absorbed shortwave radiation is the complement of this quantity.

**Model**

```
(Q, ASR)::Form0
              
α::Constant
              
ASR == (1 .- α) .* Q
```

**`Decapodes.Canon.Physics.advection`** &mdash; *Constant*.



**Advection**

[Source](https://en.wikipedia.org/wiki/Advection)

Advection refers to the transport of a bulk along a vector field.

**Model**

```
C::Form0
              
(ϕ, V)::Form1
              
ϕ == C ∧₀₁ V
```

**`Decapodes.Canon.Physics.ficks_law`** &mdash; *Constant*.



**Ficks Law**

[Source](https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion)

Equation for diffusion first stated by Adolf Fick. The diffusion flux is proportional to the concentration gradient.

**Model**

```
C::Form0
              
ϕ::Form1
              
ϕ == k(d₀(C))
```

**`Decapodes.Canon.Physics.jko_scheme`** &mdash; *Constant*.



**Jordan-Kinderlehrer-Otto**

[Source](https://www.google.com)

Jordan, R., Kinderlehrer, D., & Otto, F. (1998). The Variational Formulation of the Fokker–Planck Equation. In SIAM Journal on Mathematical Analysis (Vol. 29, Issue 1, pp. 1–17). Society for Industrial & Applied Mathematics (SIAM). https://doi.org/10.1137/s0036141096303359

**Model**

```
(ρ, Ψ)::Form0
              
β⁻¹::Constant
              
∂ₜ(ρ) == (∘(⋆, d, ⋆))(d(Ψ) ∧ ρ) + β⁻¹ * Δ(ρ)
```

**`Decapodes.Canon.Physics.lie`** &mdash; *Constant*.



**Lie**

[Source](https://en.wikipedia.org/wiki/lie_derivative)

**Model**

```
C::Form0
              
V::Form1
              
dX::Form1
              
V == ((⋆) ∘ (⋆))(C ∧ dX)
```

**`Decapodes.Canon.Physics.mohamed_flow`** &mdash; *Constant*.



**Mohamed Eq. 10, N2**

[Source](https://google.com)

**Model**

```
𝐮::Form1
              
(P, 𝑝ᵈ)::Form0
              
(negone, half, μ)::Constant
              
∂ₜ(𝐮) == 𝐮̇
              
𝑝ᵈ == P + half * i(𝐮, 𝐮)
              
𝐮̇ == μ * (∘(d, ⋆, d, ⋆))(𝐮) + negone * (⋆₁⁻¹)(𝐮 ∧₁₀ₚᵈ (⋆)(d(𝐮))) + d(𝑝ᵈ)
```

**`Decapodes.Canon.Physics.momentum`** &mdash; *Constant*.



**Momentum**

[Source](https://www.google.com)

**Model**

```
(f, b)::Form0
              
(v, V, g, Fᵥ, uˢ, v_up)::Form1
              
τ::Form2
              
U::Parameter
              
uˢ̇ == ∂ₜ(uˢ)
              
v_up == (((((((-1 * L(v, v) - L(V, v)) - L(v, V)) - f ∧ v) - (∘(⋆, d, ⋆))(uˢ) ∧ v) - d(p)) + b ∧ g) - (∘(⋆, d, ⋆))(τ)) + uˢ̇ + Fᵥ
              
uˢ̇ == force(U)
```

**`Decapodes.Canon.Physics.navier_stokes`** &mdash; *Constant*.



**Navier-Stokes**

[Source](https://en.wikipedia.org/wiki/Navier_Stokes_equation)

Partial differential equations which describe the motion of viscous fluid surfaces.

**Model**

```
(V, V̇, G)::Form1{X}
              
(ρ, ṗ, p)::Form0{X}
              
V̇ == neg₁(L₁′(V, V)) + div₁(kᵥ(Δ₁(V) + third(d₀(δ₁(V)))), avg₀₁(ρ)) + d₀(half(i₁′(V, V))) + neg₁(div₁(d₀(p), avg₀₁(ρ))) + G
              
∂ₜ(V) == V̇
              
ṗ == neg₀((⋆₀⁻¹)(L₀(V, (⋆₀)(p))))
              
∂ₜ(p) == ṗ
```

**`Decapodes.Canon.Physics.oscillator`** &mdash; *Constant*.



**Oscillator**

[Source](https://en.wikipedia.org/wiki/Harmonic_oscillator)

Equation governing the motion of an object whose acceleration is negatively-proportional to its position.

**Model**

```
X::Form0
              
V::Form0
              
k::Constant
              
∂ₜ(X) == V
              
∂ₜ(V) == -k * X
```

**`Decapodes.Canon.Physics.poiseuille`** &mdash; *Constant*.



**Poiseuille**

[Source](https://en.wikipedia.org/wiki/Hagen-Poiseuille_equation)

A relation between the pressure drop in an incompressible and Newtownian fluid in laminar flow flowing through a long cylindrical pipe.

**Model**

```
P::Form0
              
q::Form1
              
(R, μ̃)::Constant
              
Δq == Δ(q)
              
∇P == d(P)
              
∂ₜ(q) == q̇
              
q̇ == μ̃ * ∂q(Δq) + ∇P + R * q
```

**`Decapodes.Canon.Physics.poiseuille_density`** &mdash; *Constant*.



**Poiseuille Density**

[Source](https://en.wikipedia.org/wiki/hagen-poiseuille_density)

**Model**

```
q::Form1
              
(P, ρ)::Form0
              
(k, R, μ̃)::Constant
              
∂ₜ(q) == q̇
              
∇P == d(P)
              
q̇ == (μ̃ * ∂q(Δ(q)) - ∇P) + R * q
              
P == k * ρ
              
∂ₜ(ρ) == ρ̇
              
ρ_up == (∘(⋆, d, ⋆))(-1 * (ρ ∧₀₁ q))
              
ρ̇ == ∂ρ(ρ_up)
```

**`Decapodes.Canon.Physics.schroedinger`** &mdash; *Constant*.



**Schoedinger**

[Source](https://en.wikipedia.org/wiki/Schrodinger_equation)

The evolution of the wave function over time.

**Model**

```
(i, h, m)::Constant
              
V::Parameter
              
Ψ::Form0
              
∂ₜ(Ψ) == (((-1 * h ^ 2) / (2m)) * Δ(Ψ) + V * Ψ) / (i * h)
```

**`Decapodes.Canon.Physics.superposition`** &mdash; *Constant*.



**Superposition**

[Source](https://en.wikipedia.org/wiki/superposition)

**Model**

```
(C, Ċ)::Form0
              
(ϕ, ϕ₁, ϕ₂)::Form1
              
ϕ == ϕ₁ + ϕ₂
              
Ċ == (⋆₀⁻¹)(dual_d₁((⋆₁)(ϕ)))
              
∂ₜ(C) == Ċ
```




## Chemistry

**`Decapodes.Canon.Chemistry.GrayScott`** &mdash; *Constant*.



**Gray-Scott**

[Source](https://www.google.com)

A model of reaction-diffusion

**Model**

```
(U, V)::Form0
              
UV2::Form0
              
(U̇, V̇)::Form0
              
(f, k, rᵤ, rᵥ)::Constant
              
UV2 == U .* (V .* V)
              
U̇ == (rᵤ * Δ(U) - UV2) + f * (1 .- U)
              
V̇ == (rᵥ * Δ(V) + UV2) - (f + k) .* V
              
∂ₜ(U) == U̇
              
∂ₜ(V) == V̇
```

**`Decapodes.Canon.Chemistry.brusselator`** &mdash; *Constant*.



**Brusselator**

[Source](https://en.wikipedia.org/wiki/brusselator)

A model of reaction-diffusion for an oscillatory chemical system.

**Model**

```
(U, V)::Form0{X}
              
(U2V, One)::Form0{X}
              
(U̇, V̇)::Form0{X}
              
α::Constant{X}
              
F::Parameter{X}
              
U2V == (U .* U) .* V
              
U̇ == ((1 + U2V) - 4.4U) + α * Δ(U) + F
              
V̇ == (3.4U - U2V) + α * Δ(U)
              
∂ₜ(U) == U̇
              
∂ₜ(V) == V̇
```




## Biology

**`Decapodes.Canon.Biology.kealy`** &mdash; *Constant*.



**Kealy**

[Source](https://www.google.com)

**Model**

```
(n, w)::DualForm0
              
dX::Form1
              
(a, ν)::Constant
              
∂ₜ(w) == ((a - w) - w * n ^ 2) + ν * Δ(w)
```

**`Decapodes.Canon.Biology.klausmeier_2a`** &mdash; *Constant*.



**Klausmeier (Eq. 2a)**

[Source](https://www.google.com)

Klausmeier, CA. “Regular and irregular patterns in semiarid vegetation.” Science (New York, N.Y.) vol. 284,5421 (1999): 1826-8. doi:10.1126/science.284.5421.1826

**Model**

```
(n, w)::DualForm0
              
dX::Form1
              
(a, ν)::Constant
              
∂ₜ(w) == ((a - w) - w * n ^ 2) + ν * ℒ(dX, w)
```

**`Decapodes.Canon.Biology.klausmeier_2b`** &mdash; *Constant*.



**Klausmeier (Eq. 2b)**

[Source](https://www.google.com)

ibid.

**Model**

```
(n, w)::DualForm0
              
m::Constant
              
∂ₜ(n) == (w * n ^ 2 - m * n) + Δ(n)
```

**`Decapodes.Canon.Biology.lejeune`** &mdash; *Constant*.



**Lejeune**

[Source](https://www.google.com)

Lejeune, O., & Tlidi, M. (1999). A Model for the Explanation of Vegetation Stripes (Tiger Bush). Journal of Vegetation Science, 10(2), 201–208. https://doi.org/10.2307/3237141

**Model**

```
ρ::Form0
              
(μ, Λ, L)::Constant
              
∂ₜ(ρ) == (ρ * (((1 - μ) + (Λ - 1) * ρ) - ρ * ρ) + 0.5 * (L * L - ρ) * Δ(ρ)) - 0.125 * ρ * Δ(ρ) * Δ(ρ)
```

**`Decapodes.Canon.Biology.turing_continuous_ring`** &mdash; *Constant*.



**Turing Continuous Ring**

[Source](https://www.google.com)

**Model**

```
(X, Y)::Form0
              
(μ, ν, a, b, c, d)::Constant
              
∂ₜ(X) == a * X + b * Y + μ * Δ(X)
              
∂ₜ(Y) == c * X + d * Y + ν * Δ(X)
```




## Environment

**`Decapodes.Canon.Environment.boundary_conditions`** &mdash; *Constant*.



**Boundary Conditions**

[Source](https://google.com)

**Model**

```
(S, T)::Form0
              
(Ṡ, T_up)::Form0
              
v::Form1
              
v_up::Form1
              
Ṫ == ∂ₜ(T)
              
Ṡ == ∂ₜ(S)
              
v̇ == ∂ₜ(v)
              
Ṫ == ∂_spatial(T_up)
              
v̇ == ∂_noslip(v_up)
```

**`Decapodes.Canon.Environment.energy_balance`** &mdash; *Constant*.



**Energy balance**

[Source](https://google.com)

energy balance equation from Budyko Sellers

**Model**

```
(Tₛ, ASR, OLR, HT)::Form0
              
C::Constant
              
Tₛ̇ == ∂ₜ(Tₛ)
              
Tₛ̇ == ((ASR - OLR) + HT) ./ C
```

**`Decapodes.Canon.Environment.equation_of_state`** &mdash; *Constant*.



**Equation of State**

[Source](https://google.com)

**Model**

```
(b, T, S)::Form0
              
(g, α, β)::Constant
              
b == g * (α * T - β * S)
```

**`Decapodes.Canon.Environment.glen`** &mdash; *Constant*.



**Glens Law**

[Source](https://www.google.com)

Nye, J. F. (1957). The Distribution of Stress and Velocity in Glaciers and Ice-Sheets. Proceedings of the Royal Society of London. Series A, Mathematical and Physical Sciences, 239(1216), 113–133. http://www.jstor.org/stable/100184

**Model**

```
Γ::Form1
              
(A, ρ, g, n)::Constant
              
Γ == (2 / (n + 2)) * A * (ρ * g) ^ n
```

**`Decapodes.Canon.Environment.halfar_eq2`** &mdash; *Constant*.



**Halfar (Eq. 2)**

[Source](https://www.google.com)

Halfar, P. (1981), On the dynamics of the ice sheets, J. Geophys. Res., 86(C11), 11065–11072, doi:10.1029/JC086iC11p11065

**Model**

```
h::Form0
              
Γ::Form1
              
n::Constant
              
∂ₜ(h) == (∘(⋆, d, ⋆))(((Γ * d(h)) ∧ mag(♯(d(h))) ^ (n - 1)) ∧ h ^ (n + 2))
```

**`Decapodes.Canon.Environment.insolation`** &mdash; *Constant*.



**Insolation**

[Source](https://google.com)

**Model**

```
Q::Form0
              
cosϕᵖ::Constant
              
Q == 450cosϕᵖ
```

**`Decapodes.Canon.Environment.tracer`** &mdash; *Constant*.



**Tracer**

[Source](https://google.com)

**Model**

```
(c, C, F, c_up)::Form0
              
(v, V, q)::Form1
              
c_up == (((-1 * (⋆)(L(v, (⋆)(c))) - (⋆)(L(V, (⋆)(c)))) - (⋆)(L(v, (⋆)(C)))) - (∘(⋆, d, ⋆))(q)) + F
```

**`Decapodes.Canon.Environment.warming`** &mdash; *Constant*.



**Warming**

[Source](https://google.com)

**Model**

```
Tₛ::Form0
              
A::Form1
              
A == avg₀₁(5.8282 * 10 ^ (-0.236Tₛ) * 1.65e7)
```


```
[ Info: Page built in 0 seconds.
[ Info: This page was last built at 2025-01-17T11:29:36.025.
```
