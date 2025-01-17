#add parent dir to find package. Only needed for source code build, pip install doesn't need it.
import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)

import gym
import numpy as np
import pybullet_envs
import time


def relu(x):
  return np.maximum(x, 0)


class SmallReactivePolicy:
  "Simple multi-layer perceptron policy, no internal state"

  def __init__(self, observation_space, action_space):
    assert weights_dense1_w.shape == (observation_space.shape[0], 64.0)
    assert weights_dense2_w.shape == (64.0, 32.0)
    assert weights_final_w.shape == (32.0, action_space.shape[0])

  def act(self, ob):
    x = ob
    x = relu(np.dot(x, weights_dense1_w) + weights_dense1_b)
    x = relu(np.dot(x, weights_dense2_w) + weights_dense2_b)
    x = np.dot(x, weights_final_w) + weights_final_b
    return x


def main():
  env = gym.make("InvertedPendulumSwingupBulletEnv-v0")
  env.render(mode="human")

  pi = SmallReactivePolicy(env.observation_space, env.action_space)

  while 1:
    frame = 0
    score = 0
    restart_delay = 0
    obs = env.reset()

    while 1:
      time.sleep(1. / 60.)
      a = pi.act(obs)
      obs, r, done, _, _ = env.step(a)
      score += r
      frame += 1
      still_open = env.render(mode="human")
      if still_open == False:
        return
      if not done: continue
      if restart_delay == 0:
        print("score=%0.2f in %i frames" % (score, frame))
        restart_delay = 60 * 2  # 2 sec at 60 fps
      else:
        restart_delay -= 1
        if restart_delay > 0: continue
        break


# yapf: disable
weights_dense1_w = np.array(
    [[
        +0.5877, -0.5825, -0.5542, -0.2557, -0.4485, +1.4126, +0.2701, -0.6204,
        -0.2580, +0.2106, -0.2296, +0.7949, +0.6224, -0.0186, +0.4216, +1.0924,
        -0.1538, -0.2818, +0.4855, -0.2496, +0.7461, -0.6156, +0.0801, +0.7871,
        -0.4312, -0.9585, +0.1566, -0.2218, -1.0393, +0.6104, -0.5339, +0.8258,
        +0.4064, +0.0503, +0.4753, -0.8161, +0.0812, +0.2311, -0.9492, -1.1791,
        +1.2375, +0.2916, +1.2290, +0.2796, -0.8864, -1.1424, -0.5714, +0.1413,
        +0.7340, -0.4152, +0.2832, -0.3886, +0.4810, -0.7092, -0.5966, +0.1089,
        +0.1007, +0.5226, -0.3343, +0.1760, +0.4099, -0.9913, -1.1694, -1.0018
    ],
     [
         +0.4054, +0.2495, +0.5483, +0.7193, -0.1833, -0.2237, -0.4353,
         -0.1005, +0.2848, +0.3193, +0.2551, -0.1267, -0.7200, +0.3952,
         +0.3390, +0.2123, +0.1388, +0.8869, -0.1095, -0.1718, -0.4128,
         -0.7047, -1.1383, +0.6552, -0.0037, -0.4306, +0.2749, -0.9121,
         +0.4406, -0.0163, +0.4852, +0.6150, +0.1354, -0.7839, +0.2261,
         +0.3988, -0.2867, -0.5369, -0.0788, +0.0125, +0.2645, +0.1614,
         +0.7531, +0.5786, +0.6903, -0.7974, -0.2934, -0.3407, -0.7366,
         -0.1585, +1.0333, -0.0183, +0.2690, -0.5674, -0.0266, +0.0898,
         -0.1441, -0.0988, +0.7260, +0.7994, +0.1521, -0.3210, -0.1403, -0.2685
     ],
     [
         -0.1050, -0.1826, +0.4717, -0.3515, +0.9648, -0.6372, -0.4686,
         +0.6959, +0.3540, +0.3515, +0.3239, -1.6177, -0.0651, +0.4653,
         +0.5058, +0.3465, -0.6693, -0.1118, -0.9582, -1.5053, -0.2256,
         -0.1989, -0.1901, -0.4282, -1.3479, -0.5629, +0.6828, -0.3515,
         -0.4724, +0.4618, +0.3008, +0.1280, +0.3720, -0.0545, +0.3104,
         -0.2527, +0.4614, +0.4994, -0.0099, +0.4597, -0.2667, -0.0374,
         -0.3393, +0.2675, -0.2635, -0.6062, +0.6404, +0.4500, -0.5105,
         -1.5838, -0.1396, +0.8804, +0.5794, -0.6823, -0.2125, +0.4510,
         +0.2424, +0.3407, -0.3354, +0.1306, -1.0006, +0.2358, +0.6479, +0.2027
     ],
     [
         +0.7453, +0.8937, -0.9068, +0.2950, +0.4412, -0.6005, -1.3008,
         -0.0299, -0.6434, +1.4992, +0.7437, +0.4271, -0.0549, +1.2337,
         +1.6758, -0.7335, +0.2251, -1.1287, -1.0611, -0.4609, -1.6821,
         -0.3495, -0.5520, +0.2407, -1.0738, +0.9423, -0.6853, -0.0193,
         +0.6365, +0.3979, -1.8896, -1.1404, +0.4708, -0.2113, +1.3380,
         +0.6163, +0.5543, +0.4372, -0.3004, +1.0200, -0.4211, +0.5034,
         -0.1635, +2.0363, +0.1362, -0.2348, +0.7659, -1.6971, -1.3513,
         -0.2940, +1.2592, -0.3885, +0.5544, +0.8858, +0.0189, -1.8006,
         +1.3254, +0.6919, +0.3571, -0.5189, -0.0115, -1.7036, -0.8770, +1.2328
     ],
     [
         -0.3661, +0.5205, +0.6454, +0.9826, -0.2945, -0.3074, +0.6830,
         +0.3798, +0.0578, +0.2303, +0.0181, -0.3768, -0.1607, +0.9089,
         +0.2910, -0.0265, -0.7435, +0.2932, -0.4173, +0.2959, +0.2079,
         +0.2649, +0.4184, +0.5963, +0.2120, +0.1885, +0.3611, +0.5193,
         +0.4538, +0.7072, +0.2274, +0.2233, +0.3970, +0.0560, +0.2132,
         +0.0186, +0.1522, -0.2460, +0.6636, +0.4592, -0.5299, +1.1159,
         -0.2861, +0.3664, -0.0648, +0.1958, -0.0180, -0.2585, +0.1408,
         +0.2639, -0.3697, +0.4727, +1.0321, +0.0851, +0.8350, +0.0830,
         +0.1625, -0.3849, +0.3014, -0.1514, -0.5960, -0.4083, -0.1023, +0.2080
     ]])

weights_dense1_b = np.array([
    -0.4441, -0.2462, -0.2997, +0.3283, -0.2751, +0.0474, +0.0720, -0.2133,
    -0.0770, -0.0053, +0.0138, -0.3554, -0.2999, -0.2340, +0.0054, +0.4380,
    -0.1461, -0.2035, -0.8094, +0.0909, -0.1714, +0.2412, -0.1519, +0.0391,
    +0.1525, +0.1798, +0.1041, +0.4503, -0.0088, +0.0323, -0.0414, +0.4621,
    +0.1720, -0.1793, +0.1734, +0.1588, +0.2802, +0.1220, +0.1011, -0.1334,
    -0.0663, +0.4778, +0.1110, -0.1536, +0.1873, -0.0090, -0.5979, +0.3604,
    -0.2515, +0.4471, +0.2444, -0.2565, -0.1102, +0.0982, -0.0625, +0.3902,
    -0.0248, -0.2240, +0.0894, -0.0671, -0.3344, -0.0089, -0.0793, +0.2673
])

weights_dense2_w = np.array([
    [
        +0.1063, +0.2017, +0.0029, -0.2442, -0.1362, +0.2871, +0.2270, -0.1260,
        +0.5271, -0.1744, -0.4323, +0.3637, -0.0083, -0.0547, +0.4549, -0.0164,
        +0.0913, -0.1635, +0.3583, +0.3020, +0.2240, -0.3561, +0.0689, +0.0126,
        +0.0508, -1.2876, -0.0003, -0.0464, -0.2184, -0.2538, -0.5314, +0.5790
    ],
    [
        -0.2180, +0.9455, +0.1446, -0.0724, +0.3771, -0.4290, +0.3908, -0.1787,
        -0.1009, -0.0539, -0.5364, -0.5032, -0.0631, -0.1185, -0.9890, +0.1935,
        -1.3280, -0.9275, +0.0670, -0.4234, -0.2061, +0.2674, +0.2963, +0.5353,
        -0.0221, -0.3095, +0.3255, -0.4568, +0.1337, -0.2826, -0.0538, -1.2748
    ],
    [
        +0.3038, +0.0690, +0.1495, -0.1801, -0.0140, -0.1370, -0.2094, -1.9336,
        +0.2150, -0.5506, +0.3097, -0.9412, +0.1507, -0.0708, -0.8874, -0.1183,
        -0.0580, -0.7503, +0.2276, -0.3497, +0.0067, +0.2541, -0.1207, +0.5209,
        +0.5381, -1.2157, +0.4692, -0.0536, -0.2078, -0.9902, -1.0954, -1.3646
    ],
    [
        +0.0581, -1.0529, -0.0581, +0.0473, -0.1228, +0.0913, -0.7037, +0.0711,
        +0.2062, -0.2102, +0.0475, -0.5266, +0.1324, -1.7822, -0.2985, +0.0172,
        +0.0110, -0.1624, -0.3990, -0.3165, +0.1287, -0.5655, +1.3905, -1.5117,
        +0.1874, -0.5032, -0.3292, +0.3378, -0.4749, +0.0765, +0.4345, -0.1121
    ],
    [
        -0.1315, +0.2873, -1.0164, +0.2925, -0.5024, +0.2321, -1.3038, -0.7796,
        +0.0830, -0.3378, -0.1037, +0.0033, -0.7885, +0.4841, +0.1578, +0.1771,
        +0.1991, -0.1073, -0.0181, +0.0496, +0.0919, +0.0585, +0.4595, +0.1634,
        -0.2220, -0.0226, +0.4703, -1.8576, +0.3075, -0.4581, +0.2507, +0.2085
    ],
    [
        +0.2704, +0.0379, +0.2313, -0.5561, -0.7413, -0.7693, +0.4787, +0.3033,
        -1.3572, -0.1323, -0.5202, -0.6937, -0.6824, -0.1782, -1.1647, -0.3461,
        -0.8537, +0.5416, +0.0638, -0.4208, -0.4464, +0.0009, -0.4284, +0.1806,
        +0.4172, -0.5477, +0.5549, +0.1937, -0.6029, +0.2084, -0.8289, -0.4554
    ],
    [
        +0.3719, +0.4292, +0.2655, -0.1071, -0.1848, -0.0651, -0.4942, +0.0514,
        -0.1364, -0.1573, -0.0880, -0.4625, -0.0889, +0.2049, -1.2166, -0.2164,
        -0.3680, -0.7242, -0.1208, -0.3569, +0.0591, +0.3773, -1.2525, +0.4139,
        -0.1203, -0.2808, -0.2460, -0.3056, -0.2309, +0.1638, +0.1502, -0.2354
    ],
    [
        +0.2204, +0.3725, +0.1919, +0.1579, +0.0064, +0.0469, -0.5103, -0.5866,
        +0.0043, -0.2127, -0.0816, +0.4270, -0.0504, +0.2804, -0.1278, -0.0507,
        +0.1206, -0.6903, -0.2278, -0.0725, +0.2198, +0.1067, +0.2162, +0.2341,
        -0.6394, -1.2196, +0.3075, -1.0066, +0.2299, -0.1218, -0.0533, +0.3365
    ],
    [
        +0.2458, -0.1112, -0.6971, +0.1730, +0.0093, -0.0066, -0.2500, -1.2508,
        -0.0108, -0.4091, -0.5608, -0.0239, +0.4287, -0.1187, +0.0476, -0.1859,
        +0.1335, +0.0564, +0.2657, +0.3620, +0.4023, +0.0518, -0.1151, +0.0172,
        +0.0270, -0.4894, +0.3967, +0.1362, +0.1078, -1.4673, -0.6417, +0.0105
    ],
    [
        -1.2388, -0.5692, +0.2738, -0.8659, +0.1514, +0.0501, -0.3654, -0.9175,
        +0.1314, -0.4386, +0.1715, +0.2538, +0.1051, -0.1091, +0.1875, -0.0295,
        -0.4012, -0.5032, -0.6742, -0.1109, +0.1125, -0.5023, -0.2032, -0.2740,
        -0.9510, +0.9708, -0.0643, -0.5463, -0.0895, -0.7491, +0.6833, +0.1855
    ],
    [
        -0.4298, -0.0464, -0.0294, -0.0743, +0.0902, -0.6215, +0.0848, -0.3727,
        +0.2700, -0.3201, -0.2578, +0.2471, -0.6535, +0.2581, +0.2505, -0.1900,
        +0.1637, -1.5921, -0.1360, -0.0777, -0.0092, +0.0816, +0.0996, -0.0197,
        -0.7934, +0.0909, +0.2011, +0.1988, +0.1273, -0.0366, +0.0466, +0.1477
    ],
    [
        +0.1492, +0.1446, +0.4695, -0.4109, -0.0883, -0.1199, +0.5098, +0.4549,
        -0.2600, +0.1315, -0.2831, +0.4905, +0.0915, +0.1289, -1.1824, +0.3743,
        -0.3307, -0.2300, -0.6317, -0.2493, -1.2151, -0.1466, -0.4567, -1.0819,
        +0.2878, -1.0267, +0.2882, +0.5518, -0.0761, +0.3592, +0.1387, -0.6827
    ],
    [
        +0.1444, -0.1397, +0.1136, +0.0452, -0.3338, +0.1050, +0.2811, -0.1238,
        -0.4973, -0.0804, +0.0148, +0.1621, -0.8240, +0.2157, +0.1887, +0.0192,
        -1.2242, +0.2255, -0.2271, -0.4326, -0.0362, +0.0116, -0.2229, +0.4142,
        +0.3929, -0.2313, +0.1735, +0.0598, +0.1726, +0.1078, +0.1444, +0.3110
    ],
    [
        -0.7894, -0.0617, +0.3583, -0.7723, +0.1178, +0.0533, -0.2285, -1.2298,
        +0.1727, -0.3313, +0.1193, -0.6488, +0.2996, -0.5132, -0.3868, +0.0174,
        +0.1475, +0.3516, -0.5912, -0.8573, +0.0606, -0.0528, -0.1981, +0.0196,
        -0.1688, -0.3554, -0.0234, -0.7206, +0.2903, -0.9404, -1.5141, -0.2722
    ],
    [
        -1.2703, -0.7481, +0.4099, -0.7886, +0.2750, -0.0530, -0.6855, -0.7960,
        +0.2931, +0.0986, +0.2574, +0.3546, -0.1636, -0.6219, +0.3183, +0.1384,
        -0.0684, -1.2439, -0.8255, -0.1529, +0.2066, -0.4686, +0.3696, -0.2439,
        -1.6751, +0.7610, -0.5769, -0.5236, +0.2315, -0.4293, +0.7452, +0.6290
    ],
    [
        +0.1636, -0.0258, -0.0946, +0.5087, -0.2138, -0.5867, -0.1223, +0.0970,
        -0.5604, -0.3155, +0.2778, +0.2844, -0.6220, +0.0870, +0.1567, -0.8622,
        +0.2385, +0.3428, +0.1315, +0.2830, -0.3414, -0.1083, -0.0021, +0.4448,
        -0.1093, +0.5797, +0.5512, +0.0886, +0.2515, -0.1098, -0.5983, -0.1664
    ],
    [
        +0.0332, -0.1306, +0.2431, -0.5394, -0.2755, -0.4544, +0.3230, +0.0475,
        -0.4289, +0.1263, -0.7816, +0.2001, +0.1425, +0.2706, -1.0709, -0.3947,
        -1.3802, -0.1414, -0.1457, -0.7114, -0.6793, -0.0257, -0.8971, -0.2432,
        +0.0006, -0.3711, +0.2958, -0.0177, +0.1747, -0.0733, -0.3160, -0.6292
    ],
    [
        +0.2540, +0.4159, -0.4193, +0.4756, -0.5615, -0.0777, -0.1692, -0.2047,
        -0.6844, -0.2723, +0.0727, -0.1912, +0.0989, +0.1546, +0.4719, -0.2639,
        -0.1997, +0.2235, +0.5461, +0.2992, -1.6747, -0.3055, -0.7582, +0.0934,
        +0.2088, -0.2527, +0.2810, -0.0126, -0.2710, -0.7904, -0.2154, -0.5613
    ],
    [
        -0.2470, +0.1133, -0.1563, -0.4254, +0.5442, +0.1291, +0.2176, +0.0374,
        -0.8939, -0.4140, +0.1537, -0.1740, +0.9369, -0.0037, -0.4261, -0.7104,
        -0.7777, +0.1905, -0.5320, -0.1168, +0.0347, -0.0454, -0.3947, -0.6101,
        +0.2560, -0.2748, -0.0115, +0.0442, -0.0840, -0.0564, -0.2105, -0.3223
    ],
    [
        -0.0404, +0.1026, -0.3563, -0.2962, -0.7801, -0.2794, -0.1065, +0.4522,
        +0.2426, +0.1916, -0.8589, +0.1918, +0.4101, -0.1290, -0.3302, +0.1000,
        -0.0601, -0.2014, -0.7935, +0.4843, -0.6731, +0.2180, +0.1019, -0.2928,
        +0.0366, -0.4442, -0.0406, -0.4545, -0.2187, +0.1910, +0.9510, -0.1191
    ],
    [
        +0.0344, -0.6187, -0.1423, +0.3670, -0.7356, -0.0288, -0.1769, -0.9789,
        -1.3008, -0.4707, +0.1346, -0.1823, -0.2180, -0.4896, -0.0455, -0.7968,
        -0.3335, +0.6360, +0.2356, -0.0207, -0.2652, +0.2302, -0.3929, +0.2243,
        +0.6438, +0.7061, +0.2904, +0.1324, -0.4476, +0.2047, -0.6898, -0.6214
    ],
    [
        -0.0215, -0.7005, -0.0687, +0.0166, -0.3514, -0.0745, +0.0922, +0.5453,
        +0.0969, +0.0386, -0.0103, +0.1984, -1.0903, -0.2738, -0.4855, +0.3083,
        +0.2451, +0.5611, -0.3741, +0.2794, +0.0953, -0.3711, -0.1832, -0.2603,
        +0.3729, +0.2859, -0.3258, -1.2615, +0.0928, -0.1043, +0.1818, +0.1052
    ],
    [
        +0.2063, -0.4528, -0.0057, -0.0972, -0.1732, +0.0062, -0.5985, +0.2504,
        -0.3243, -0.5488, -0.1981, +0.0969, -0.8003, -0.2163, -0.6253, +0.1420,
        -0.1593, +0.1623, -0.0719, +0.0738, +0.3514, -0.4224, +0.0098, -0.0067,
        +0.2754, +0.1454, -0.3292, -0.0407, -0.7088, +0.7650, -0.0182, -0.0452
    ],
    [
        -0.1059, -0.6218, +0.1371, -0.2479, -0.0653, -0.0035, -0.3983, +0.0243,
        -0.2188, -0.3608, +0.3230, -0.6048, +0.0848, -0.9398, +0.1182, -0.2141,
        +0.0755, +0.1749, -0.5544, +0.0777, +0.0288, -0.4650, -0.1328, +0.0272,
        -0.1134, -0.5497, -0.7305, +0.2035, -0.1138, -0.3764, -0.1077, -0.0619
    ],
    [
        -0.2962, -0.2979, -0.5164, -1.1713, -1.1070, -0.3612, +0.0832, +0.5215,
        +0.4963, +0.1109, -2.0335, +0.0426, +0.6391, +0.1183, -0.3604, -0.0953,
        +0.1748, +0.1531, +0.1823, +0.3383, -0.3340, -0.1464, +0.0583, -0.7169,
        +0.1044, -0.1128, +0.1358, -0.5949, -0.5330, +0.0007, +0.4265, -0.1255
    ],
    [
        -0.6321, -0.4892, -0.1697, -0.0665, -0.1715, -0.0042, -0.1025, +0.2831,
        +0.3383, +0.0200, +0.3494, +0.2269, +0.0419, +0.0365, -0.4095, +0.2798,
        -0.3788, +0.0791, -0.6231, -0.0929, -0.2438, -0.3717, +1.1090, -0.7410,
        +0.5276, -0.0525, +0.1586, -0.7940, -0.1403, +0.5189, +0.4408, +0.2783
    ],
    [
        +0.0863, -0.1234, +0.1770, +0.1606, -0.0455, -0.0650, -0.5722, -1.1812,
        +0.1314, -0.7228, +0.3411, -0.0359, -0.0146, +0.0060, +0.2504, -0.1236,
        +0.2839, -0.7190, +0.0244, +0.0833, +0.0597, +0.0164, +0.1194, +0.2457,
        -0.8212, -1.6772, +0.3122, -0.0719, +0.1411, -0.3111, -1.3788, +0.1171
    ],
    [
        -0.4888, -1.0319, -0.1769, +0.1639, +0.0734, -0.4566, -1.0295, +0.5195,
        -0.5277, +0.0296, -0.0732, +0.2698, -0.4389, -0.6899, -0.6707, +0.0360,
        -0.0028, -0.6112, -0.8115, -0.2616, -0.0706, -0.5321, -0.2747, -1.1524,
        -0.0645, -0.0421, -0.3517, -0.4075, -0.1166, +0.6472, +0.0250, -0.3585
    ],
    [
        -0.3122, -0.2761, -0.0860, -0.2080, -0.2592, -0.1262, -0.0000, +0.0064,
        +0.3869, -0.0712, +0.0700, -0.9122, +0.1585, -1.0705, -0.4595, +0.1414,
        -0.4563, -0.3509, +0.1370, -0.4546, +0.0924, -0.5005, +0.8518, -1.4722,
        +0.4280, -0.2569, -0.1950, -0.3892, +0.0974, +0.0142, -0.0750, -1.0935
    ],
    [
        -0.2389, -0.1222, +0.1513, -1.0903, -0.0777, +0.2233, -0.2945, -1.0573,
        -0.6673, -0.9787, +0.4047, -1.2823, +0.0238, -0.9849, +0.1218, -0.0379,
        +0.1686, -1.5184, -0.0359, -0.2899, -0.0147, -0.2620, -0.0294, +0.1790,
        -0.4546, -0.1393, -0.2614, -0.1130, +0.3277, -0.5504, -1.4897, +0.4290
    ],
    [
        +0.3427, -0.1801, -0.9729, -0.2763, -0.8175, -0.2292, -0.2283, -1.0905,
        -0.3877, -0.3596, -0.0185, -0.5790, -0.1083, +0.1029, +0.2087, -0.2265,
        +0.3843, +0.3569, +0.4135, +0.1367, +0.1019, -0.0472, -0.1326, +0.3414,
        +0.3957, +0.2921, +0.2106, -0.0877, -0.3301, -1.3795, -1.9779, -0.4937
    ],
    [
        +0.1940, -0.2997, -0.4792, +0.2675, -0.6258, -0.0457, -0.5112, -0.0076,
        -0.6497, -0.7706, +0.1871, -0.1602, -0.0135, +0.4243, -0.5747, -0.5883,
        +0.4021, -0.2582, +0.3381, +0.3950, +0.0503, +0.0106, +0.2930, +0.2948,
        +0.0231, +0.4963, +0.6190, +0.3516, -0.9469, -0.0323, -0.0254, -0.3314
    ],
    [
        -0.0666, -0.3086, +0.0050, -0.7425, +0.0498, -0.1735, +0.0643, -0.7302,
        -0.2838, -0.4926, +0.2588, -1.0888, +0.0914, -0.2110, +0.3146, +0.0769,
        +0.1527, -0.7908, +0.1144, -0.4159, -0.1099, -0.2469, +0.1520, +0.3110,
        -0.6905, +0.1466, -0.1214, -0.5032, +0.0486, -0.3263, +0.0748, +0.4858
    ],
    [
        +0.3977, -0.0844, +0.0825, -0.0687, -0.8396, +0.2654, -0.0521, -0.1041,
        -0.5838, -0.3881, -0.0133, +0.0767, +0.3582, +0.1250, -0.3787, +0.2232,
        -1.6387, +0.1836, -0.2685, -0.4428, +0.1816, -0.1108, +0.1340, +0.0555,
        -0.0085, +0.0386, +0.1277, +0.0295, -0.7560, +0.0657, +0.0095, +0.0913
    ],
    [
        -0.3619, +0.2578, +0.3163, +0.1775, +0.1437, -0.1839, +0.1491, -0.4246,
        +0.3383, -0.5554, +0.2321, +0.2196, -0.2709, -0.0673, +0.0790, +0.0549,
        +0.0146, -1.4400, -0.3682, -0.4452, +0.1132, -0.0693, +0.4161, -0.0508,
        -0.2573, +0.3547, +0.2300, -0.0433, +0.3701, -0.0716, +0.0865, +0.3202
    ],
    [
        -0.2407, -0.3514, -0.2882, -0.1980, +0.3598, -0.3302, +0.3311, +0.1154,
        +0.1423, -0.2290, -0.6468, +0.2341, +0.0219, -0.3510, -0.8240, +0.1463,
        -0.3198, -0.0513, -0.9552, -0.2212, -0.1091, -0.5052, +0.1874, -0.1514,
        -0.7181, +0.1132, -0.5173, +0.2874, +0.4601, +0.3317, +0.1209, -0.4715
    ],
    [
        +0.4039, -0.0515, -0.1019, +0.4119, +0.1023, -0.0505, +0.3062, -0.5871,
        -0.3284, -0.6936, -0.2142, -0.0067, -0.8245, +0.0604, +0.2082, +0.2818,
        +0.4094, -1.2403, +0.2902, -0.4497, +0.3492, -0.2630, +0.2257, +0.2616,
        -0.0756, +0.3950, +0.1607, -0.4299, -0.0042, -0.3791, +0.0144, +0.3923
    ],
    [
        +0.2782, -0.1456, -0.0002, +0.3011, -0.2252, +0.0572, +0.1349, -0.1567,
        -0.2850, -0.2994, +0.1602, -0.0868, -0.5167, +0.4240, +0.2210, +0.1657,
        +0.0883, -0.1288, -0.0227, -0.3949, +0.1043, -0.1381, +0.0739, -0.0357,
        -0.1723, -0.2657, +0.1199, -0.1253, -0.8570, +0.1793, +0.0042, +0.2571
    ],
    [
        +0.1808, +0.0781, -0.0530, +0.3645, -0.0659, -0.0229, +0.0723, -0.2956,
        +0.0014, +0.0886, -0.2523, -1.1491, +0.1169, +0.1121, -0.8267, +0.0281,
        -0.1044, -0.2294, +0.0513, -0.9215, +0.2674, +0.0013, -0.0650, +0.2553,
        +0.0816, -0.7934, +0.2155, -1.3771, -0.1983, -0.3055, +0.2549, +0.0883
    ],
    [
        -0.1989, -0.3779, +0.2484, +0.0978, +0.3002, -0.2595, -0.0993, -0.7726,
        -0.0245, -0.6115, +0.0579, -0.7989, -0.0208, -0.0149, -1.4722, +0.3503,
        -0.1758, -0.4039, -1.9504, -0.2489, -0.2551, +0.0146, -0.1026, -0.6208,
        +0.3920, -0.8281, -0.3682, -0.3127, +0.1773, -0.0195, -0.3558, -0.4386
    ],
    [
        +0.3965, +0.2776, -0.0051, -0.3705, -0.3877, +0.0462, +0.2481, +0.0638,
        -0.5678, +0.2069, -0.2101, -0.3165, +0.0694, +0.3458, -1.0740, -0.2276,
        -0.2802, +0.1290, +0.3323, -0.6620, -1.0497, +0.0449, -1.4877, +0.6505,
        -0.0039, -0.5675, +0.1965, +0.1813, -0.1576, +0.2611, +0.0413, -0.7096
    ],
    [
        -0.2771, -0.2090, +0.3171, -1.1884, +0.0306, -0.0635, -0.3072, +0.1631,
        -0.3107, -0.4344, +0.0475, -1.1032, +0.0050, -1.6227, -0.2919, +0.1205,
        +0.2610, -0.8912, -0.0364, -0.0302, +0.2187, -0.3477, -0.2162, +0.0541,
        -0.1731, -0.5533, -1.1136, -0.3114, -0.0904, +0.0234, -0.1263, -0.4608
    ],
    [
        +0.2534, +0.2506, -0.5988, +0.3239, -0.5094, +0.2584, -0.1520, -0.3674,
        -0.5281, -0.2938, -0.0664, +0.3468, +0.1871, +0.4229, -1.1005, +0.0895,
        -0.1058, -0.2018, +0.5277, +0.1065, -2.9736, +0.0834, -0.4339, +0.5220,
        -0.3065, +0.0976, +0.4859, -0.0876, -0.5134, +0.0273, -0.4311, -0.0629
    ],
    [
        -1.0013, -0.7660, +0.4058, -3.0321, +0.0533, +0.0794, -1.2917, -1.0423,
        +0.0235, -0.2441, +0.2986, +0.2793, +0.3185, -0.7738, +0.0709, +0.1806,
        +0.0065, -0.3429, -0.5904, -0.2240, -0.2247, -0.1551, +0.2479, -0.7799,
        -0.4368, +0.2717, -0.3030, +0.2230, -0.1252, -0.1713, -0.4256, +0.0946
    ],
    [
        -0.5044, -0.3197, -0.0715, -0.0414, -0.2140, -0.2098, +0.3549, +0.0071,
        +0.2459, +0.0855, -0.4905, +0.4785, -0.0644, -0.0442, -0.5088, +0.1229,
        +0.3045, +0.0949, +0.5608, +0.0035, +0.2524, -0.1201, +0.4582, -0.9841,
        -0.2432, -0.4455, +0.1591, -0.0743, +0.1235, +0.1924, -0.2510, -0.0401
    ],
    [
        +0.5910, -0.1650, -0.3341, +0.3136, -0.0819, -0.1846, -0.3609, +0.2772,
        -0.0841, +0.0612, -1.0691, +0.0500, -0.9307, +0.4375, -0.9497, -0.0597,
        -0.7687, +0.2086, +0.2169, -0.2657, -0.5765, -0.1814, -1.1223, +0.2315,
        +0.8662, +0.0936, +0.0851, -1.8539, -0.0759, +0.4064, +0.2069, -0.8922
    ],
    [
        -0.1478, +0.3415, -0.2042, +0.5568, -0.7672, -0.1465, -0.1311, -0.2273,
        +0.0602, -0.2321, -0.2689, +0.1515, -1.0434, +0.2948, -0.4986, +0.1426,
        -0.7398, -0.4810, -0.0648, -0.3290, -0.1646, -0.1314, +0.0100, +0.3540,
        -0.2790, -0.0118, +0.4205, -0.5476, -0.1409, -0.1341, +0.3308, +0.1991
    ],
    [
        +0.1532, -0.2862, -1.0844, +0.2213, -1.5302, -0.1382, -0.3119, -1.5098,
        -0.5984, -0.8033, +0.0835, -0.5982, -0.9022, +0.0325, -0.0693, -0.7834,
        +0.2342, +0.2223, +0.3314, +0.1252, +0.2134, -0.1843, -0.2085, +0.3213,
        +0.2308, +0.4200, +0.0852, -0.1438, -0.4427, +0.2863, -0.6166, -0.2677
    ],
    [
        +0.2118, -0.5590, -0.3589, +0.1854, -1.1902, -0.2337, +0.3533, -0.0890,
        -0.3013, +0.4551, -0.2130, -1.0383, -0.2290, -0.1976, -1.3175, -0.5657,
        -0.2857, +0.5560, +0.1437, -0.3211, +0.1788, -0.1494, -1.0336, +0.2679,
        +0.5221, +0.5256, +0.1761, -0.0573, -0.2895, -0.0307, -0.2395, -0.8144
    ],
    [
        -0.6139, -1.0856, -0.5362, -1.1959, -0.3413, -0.2647, -0.3687, +0.4510,
        +0.0818, +0.0710, -0.3482, -0.0611, +0.0474, -0.7248, -0.3042, -0.0303,
        -0.3762, +0.1941, -0.8735, +0.1872, -0.3612, -0.4090, +0.2817, -0.5842,
        +0.5135, +0.8080, -0.9240, -0.1925, -0.6654, +0.4267, +0.5304, -0.3396
    ],
    [
        +0.1054, -0.1771, -0.1990, +0.3935, -0.1743, +0.0638, +0.3047, -0.0899,
        +0.4220, +0.1633, +0.1666, +0.1688, +0.0731, -0.0455, +0.2421, +0.4481,
        +0.5427, -0.1530, -0.1694, +0.4192, -0.3225, +0.1410, +0.2042, -2.2442,
        -0.4848, -0.9054, -0.2178, +0.3965, +0.4502, +0.1305, -0.0444, +0.1641
    ],
    [
        +0.1336, +0.4509, +0.0056, +0.0940, -0.3145, -0.1580, -0.1152, -0.2864,
        -0.0145, -0.3372, +0.1072, -0.3662, -0.9957, +0.3660, +0.1886, -0.2086,
        +0.2193, -0.6053, +0.0879, +0.0350, +0.0216, +0.3407, -0.0691, +0.1355,
        -0.2493, -1.5064, +0.3744, -0.2654, -0.1921, -0.6361, -0.6030, +0.3290
    ],
    [
        -0.4868, -0.0926, +0.1334, -0.8699, +0.0689, +0.1350, +0.0003, -1.6050,
        -0.2677, -0.6097, +0.0119, -1.0122, -0.1318, -0.8405, -0.1366, -0.1088,
        +0.0375, -1.0216, -0.0891, -0.2447, -0.0060, -0.3751, +0.1240, +0.0514,
        -0.5080, -1.2536, +0.4369, -0.1020, +0.1563, -0.6330, -2.3150, +0.0109
    ],
    [
        -0.5112, +0.0425, -0.1887, -0.0305, +0.0264, +0.3452, -0.0750, +0.4954,
        +0.4284, -0.0069, +0.2399, +0.9169, -0.3441, +0.0420, -0.3492, +0.4726,
        -0.1203, -0.0110, -1.1251, -0.1880, -0.2703, -0.1990, +0.8598, -0.0085,
        +0.4910, -0.1798, +0.1495, -0.4904, -0.3907, +0.5274, +0.4777, +0.4670
    ],
    [
        +0.4048, -0.2962, -0.0535, +0.3467, -0.0456, -0.0875, -0.0220, -0.2064,
        -0.8052, -0.2940, -0.1660, -1.3446, -0.0124, -0.3980, -0.0199, +0.0871,
        -0.4781, -1.0247, +0.2848, -0.2992, -0.1778, -0.0626, -0.0618, +0.0792,
        -0.7679, -1.4193, +0.0787, -0.3910, -0.1448, -0.2650, -0.3079, -1.2104
    ],
    [
        +0.4581, -0.6689, -0.1144, -0.1282, -2.0230, -0.1221, -0.2954, -1.2605,
        -1.0560, -0.8669, +0.2610, -0.3799, -0.2883, -0.2970, +0.1364, -1.5987,
        +0.2303, +0.6106, +0.3841, +0.0955, -0.3148, -0.2655, +0.0052, +0.2312,
        +0.1658, +0.4766, +0.1847, -0.1055, -0.8075, -0.1123, -0.6706, -0.6556
    ],
    [
        +0.1192, -0.1971, +0.4472, +0.1296, +0.0370, -0.1341, -0.7736, -0.1778,
        -0.0172, -0.2200, +0.1248, -0.4126, -0.3722, -0.2830, +0.0294, +0.2753,
        -0.2527, -1.0083, -0.7886, -1.5356, +0.0627, -0.2736, +0.4009, -0.4766,
        -0.2815, +0.8060, -0.0681, -0.8295, +0.4980, -0.0494, +0.4414, +0.4709
    ],
    [
        -0.2893, -0.0060, +0.1617, +0.3636, -0.0534, -0.1653, +0.2161, -0.2260,
        +0.0668, -0.3423, +0.0087, +0.3678, -0.1448, +0.3106, +0.2831, +0.0889,
        -0.1325, -0.0667, -0.1139, +0.1482, +0.1164, -0.1613, +0.0733, +0.0005,
        -0.0419, -0.0656, +0.0986, -0.1560, -0.1506, -0.1254, -0.0902, +0.2643
    ],
    [
        -0.2274, -0.5965, -0.0342, -0.6827, -0.1276, +0.0802, -1.2401, +0.2169,
        +0.0531, -0.0964, +0.2187, +0.0299, +0.2797, -0.7842, -0.5032, +0.1321,
        -0.2005, -0.3383, -0.3343, +0.1237, -0.0915, -0.6670, +0.0473, -0.6602,
        +0.1260, -1.2568, -0.2235, +0.1255, +0.3263, +0.1078, -0.0685, -0.0085
    ],
    [
        +0.3530, -0.3798, -0.5576, +0.1040, -0.1875, +0.1399, -0.1539, -1.3570,
        -0.1105, +0.0370, -0.4067, +0.2991, +0.2811, +0.1082, -0.0573, +0.2104,
        -0.1550, +0.3365, +0.5019, +0.4842, +0.4671, +0.2578, -0.0029, +0.0016,
        -0.1533, -0.2459, +0.1866, +0.0699, -0.1873, -1.1082, -0.9151, -0.1758
    ],
    [
        +0.2397, +0.2045, -0.2370, -0.3293, -0.3153, -0.2131, +0.1407, -0.0721,
        +0.0723, -0.0019, -0.3940, +0.1340, +0.3550, +0.1190, -0.6068, -0.0747,
        -0.7712, +0.1922, +0.6519, -0.0651, -0.4332, +0.0494, -0.7192, +0.4279,
        -0.1762, -0.5548, +0.1749, -0.2149, -0.6916, -0.0448, -0.1025, +0.0212
    ],
    [
        -0.1101, -0.2853, -0.3405, +0.3059, -0.5009, +0.1139, +0.0602, -0.5256,
        -0.9340, +0.1189, -0.9900, -0.5092, -1.9114, +0.1249, -0.7890, -1.1437,
        -0.4686, +0.3687, -0.2993, -0.1058, +0.0966, -0.0284, -0.4845, -0.1683,
        +0.3489, -0.0173, -0.0521, -0.1265, -0.0182, -0.2870, +0.0246, -1.0009
    ],
    [
        -0.1411, +0.1840, -0.3968, +0.2893, -0.9532, -0.2235, -0.1156, -0.7018,
        -0.2859, -0.1742, -0.6094, -0.0247, -1.0472, +0.1916, -0.4825, -0.4209,
        +0.2371, +0.0900, +0.0646, -0.1665, +0.5168, +0.0670, -0.1779, +0.3494,
        +0.3035, +0.0548, +0.2939, -0.3871, -0.0828, -0.5370, +0.0804, -0.2175
    ],
    [
        +0.4992, +0.1187, -0.0464, +0.7284, +0.1106, -0.0542, -0.3548, +0.3451,
        +0.0281, -0.4796, -0.2282, -0.3789, -0.1253, -0.0824, -0.3919, +0.1890,
        -0.1683, -2.1362, -0.9594, -0.6882, +0.6158, -0.2412, +0.2336, -0.0142,
        -0.9257, +0.3819, -0.1836, -0.7676, +0.3713, -0.1364, +0.3317, +0.3696
    ]
])

weights_dense2_b = np.array([
    -0.0528, +0.0930, -0.3614, +0.2145, -0.3644, -0.0033, -0.0702, -0.0928,
    -0.1018, +0.0424, +0.0130, +0.2634, -0.1167, +0.2412, +0.0852, +0.0047,
    +0.1958, -0.1322, +0.0218, +0.2207, +0.1946, +0.0936, +0.2900, +0.2404,
    -0.1711, +0.1214, +0.2968, -0.2935, -0.0390, +0.1330, +0.0325, +0.2185
])

weights_final_w = np.array([[-0.2378], [+0.1955], [-0.2006], [-0.5372],
                            [-0.3298], [+0.0891], [-0.3930], [+0.8978],
                            [+0.3177], [+0.5357], [+0.2878], [+0.4998],
                            [+0.2550], [-0.2619], [+1.1990], [+0.3115],
                            [+0.3655], [+0.5774], [-0.4641], [+0.2613],
                            [+0.1928], [+0.1458], [+0.4138], [-0.4969],
                            [+0.4147], [+1.0689], [-0.1562], [-0.3669],
                            [-0.3073], [+0.3354], [+0.9354], [+0.8831]])

weights_final_b = np.array([+0.2753])
# yapf: enable

if __name__ == "__main__":
  main()
