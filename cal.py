def determineCmaxCmin(Cp_o, Cp_i, m_o, m_i):
    if Cp_o * m_o < Cp_i * m_i:
        C_min = Cp_o * m_o
        C_max = Cp_i * m_i

    if Cp_o * m_o > Cp_i * m_i:
        C_min = Cp_i * m_i
        C_max = Cp_o * m_o      

    # fix
    else:
        C_min = Cp_o * m_o
        C_max = Cp_i * m_i

    # Cp_o Specific heat of air
    # Cp_i Specific heat of water
    # m_o Mass flow rate of air
    # m_i Mass flow rate of water
    # C_max: bigger heat capacity between hot stream and cold stream
    # C_min: smaller heat capacity between hot stream and cold stream

    return C_min, C_max

def C_r(C_min, C_max):
    ratio = C_min / C_max
    return ratio
    # C_r: capacity ratio

def Q_o(m_o, Cp_o, T_o2, T_o1):
    return m_o * Cp_o * (T_o2 - T_o1)
    # 1 inlet
    # 2 outlet

def Q_i(m_i, Cp_i, T_i2, T_i1):
    return m_i * Cp_i * (T_i2 - T_i1)
    # 1 inlet
    # 2 outlet

def Q_ave(Q_o, Q_i):
    return Q_o / 2 + Q_i / 2

def Q_max(C_min, T_i1, T_o1):
    return C_min * (T_i1 - T_o1)

def epsilon(Q_ave, Q_max):
    return Q_ave / Q_max

def equation(C_r, epsilon, NTU_eq):
    term1 = NTU_eq ** 0.22 / C_r
    term2 = np.exp(-C_r * NTU_eq ** 0.78) - 1
    return 1 - np.exp(term1 * term2) - epsilon

def NTU(C_r, epsilon, NTU_eq):
    initial_guess = 1
    NTU_solution = fsolve(equation, initial_guess, args=(C_r, epsilon, NTU_eq))
    return NTU_solution










#王博ppt p68 p94