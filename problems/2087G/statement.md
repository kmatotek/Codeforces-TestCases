# Problem Description

Recently, esports has been recognized as an official sport in Berland, and regular competitions have begun to take place. Riding the wave of popularity, Monocarp also decided to participate in the upcoming competitions (besides, prizes have never hurt anyone).
In each of the followingndays, one competition will be held. Monocarp would like to participate in all of them, but unfortunately, his current skill levelsis0. At the same time, the prize money Monocarp can earn in competitions depends on his skill level. Therefore, Monocarp decided that he could sacrifice participating in some competitions to train and increase his skill level on those days.
In general, on thei-th day, Monocarp can:
Help Monocarp calculate his maximum total income and the number of training plans with such income. Two training plans are considered different if there exists a day that is a training day in one plan and a competition day in the other one.

## Input
The first line contains a single integern(1≤n≤2⋅105) — the number of days when competitions will take place.
The second line containsnintegersa1,a2,…,an(0≤ai≤106) — the base prize money that Monocarp can expect.

## Output
Print two integers — the maximum total income that Monocarp can achieve with an optimal training plan and the number of such plans.
Since the number of plans may be too big, print it modulo998244353.