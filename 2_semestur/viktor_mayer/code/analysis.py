from uncertainties import ufloat

M = 1489*ufloat(40, 0.5)/10**9
p_0 = 10**5
T = ufloat(26+273.15, 1)
p_atm = ufloat(713.1, 0.05) * 133.322
e = ufloat(3365, 1)     
h = ufloat(8, 0.1)/100
g = ufloat(9.81, 0.005)
V = ufloat(9.8, 0.05)/10**6 
T_0 = 273.15
rho_0 = 1.293
rho = 1000

theta = (M*p_0*T)/((p_atm - e - rho*g*h)*V*T_0*rho_0)

print(theta)
print(theta.nominal_value)
print(100*2*theta.std_dev/theta.nominal_value)

    
