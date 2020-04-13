## What does the Compiler(编译器) do

![](https://qbrsjq.sn.files.1drv.com/y4mVVNnKHnq2y_sibaKbpAzfZDiG0h1YtzVbJr20svUtZA8iiUMJwmATPF5nKFfYjvnwXL2azX18pSPWFsUsvkfpzN36TWlcaN118ARPnTOgoF4544YvLzoU4sBxhc0PSeXxZodOM-4I3euzCIih62drv_-pk9fBJKJobBoK3Rl8blEppvvTb9ax5BjP0d6mak0bT5L_8623s5JDC2dtmJamg?width=431&height=81&cropmode=none)



## What does the Interpreter(解释器) do

![](https://sxrkjq.sn.files.1drv.com/y4m2GB75J-P8vrKWS9S3rfC4lbywlQmkO_aS9GgBVRrqxLiFfsYBwNOPiwHlxdJ28j8ZAYg_OV41v9-MK4N9Vk09U1ccVvfNoEChHpAyS-M23o_hhO03cUuEfDRxD-hX1Nsuh0Ss4b-jglzitlAW2u1zQs4KuSzvKBztBAZxGvXnQE27lQXYEYRZwmL_oc3m6uo1sKzZl7ztA_uvlPradfPSg?width=281&height=81&cropmode=none)

## CODE

In calc1.py, we will make a calculator, such that,

```
> 3+4
7

> 3+5
8

> 3+9
12
```



该程序的运作是这样的

对于 a + b (a,b are Integers), 通过 `词法分析` 获得了

```
(value = a, type = Integer)
(value = "+", type = PLUS)
(value = b, type = Integer)
```

这样计算就很方便了

## Source

https://ruslanspivak.com/lsbasi-part1/