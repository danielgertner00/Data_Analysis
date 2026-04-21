def s_kon(wiek,k1,k2,k3,k4):
    m1 = {'20s': 42.69,
          '30s': 39.22,
          '40s': 34.73,
          '50s': 30.83}
    sd1 = {'20s': 11.25,
          '30s': 10.89,
          '40s': 10.52,
          '50s': 10.09}
    m2 = {'20s': 42.27,
          '30s': 39.53,
          '40s': 35.08,
          '50s': 31.37}
    sd2 = {'20s': 11.75,
          '30s': 10.88,
          '40s': 9.97,
          '50s': 9.74}
    m3 = {'20s': 40.71,
          '30s': 38.89,
          '40s': 34.48,
          '50s': 30.85}
    sd3 = {'20s': 11.56,
          '30s': 10.31,
          '40s': 9.71,
          '50s': 9.72}
    m4 = {'20s': 39.42,
          '30s': 37.88,
          '40s': 33.91,
          '50s': 30.38}
    sd4 = {'20s': 10.81,
          '30s': 10.47,
          '40s': 9.52,
          '50s': 9.72}

    if 20 <= wiek <= 29:
        key = '20s'
    elif 30 <= wiek <= 39:
        key = '30s'
    elif 40 <= wiek <= 49:
        key = '40s'
    elif 50 <= wiek <= 59:
        key = '50'
    else:
        raise ValueError('Age out of bounds (20-59)')

    mean_vals = (m1[key], m2[key], m3[key], m4[key])
    sd_vals = (sd1[key], sd2[key], sd3[key], sd4[key])

    diffs = (
        k1 - mean_vals[0],
        k2 - mean_vals[1],
        k3 - mean_vals[2],
        k4 - mean_vals[3]
    )

    avg_diff = (
    (diffs[0] + diffs[1] + diffs[2] + diffs[3]) / 4
    )

    diffs_corr = (
        diffs[0] - avg_diff,
        diffs[1] - avg_diff,
        diffs[2] - avg_diff,
        diffs[3] - avg_diff
    )

    diffs_standard = (
        round((diffs_corr[0] / sd_vals[0]) * 15, 2),
        round((diffs_corr[1] / sd_vals[1]) * 15, 2),
        round((diffs_corr[2] / sd_vals[2]) * 15, 2),
        round((diffs_corr[3] / sd_vals[3]) * 15, 2)
    )

    return diffs_standard