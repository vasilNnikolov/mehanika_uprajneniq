from uncertainties import ufloat
def ice_uncertainty():
    m_h20 = ufloat(150, 0.1) 
    m_d = ufloat(20, 1)
    T_0 = ufloat(56.7, 0.1)
    T_1 = ufloat(26.1, 0.1)
    m_ice = ufloat(49, 0.1)
    T_melt = 0
    c_h20 = 4.1379
    l = (c_h20*(m_h20 + m_d)*(T_0 - T_1) + c_h20*m_ice*(T_melt - T_1))/(m_ice)
    print(l)

def steam_uncertainty():
    m_h20 = ufloat(150.8, 0.1) 
    m_d = ufloat(20, 1)
    T_0 = ufloat(19.6, 0.1)
    T_1 = ufloat(65.6, 0.1)
    m_ice = ufloat(14.2, 0.2)
    T_melt = ufloat(98.07, 0.1) 
    c_h20 = 4.1379
    l = (c_h20*(m_h20 + m_d)*(T_1 - T_0) + c_h20*m_ice*(T_1 - T_melt))/(m_ice)
    print(l)
if __name__ == "__main__":
    steam_uncertainty()