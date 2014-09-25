import numpy 

#-------------------------------------------------
def Bnu(nu,T):  # Calculate the planck blackbody brightness in W/m^2/sr/Hz
    '''
    Planck blackbody brightness function (2 polarizations, in W/m^2/sr/Hz).
    Frequency (nu) must be in Hz.
    Bnu(nu,T) = 2.*(h*nu)*(nu/c)**2 * (1./(numpy.exp(x) - 1.))
    '''
    "Blackbody brightness function (2 polarization, in W/m^2/sr/Hz)"

    # Frequency vector must be in Hz.
    # Physical constants in SI units
    c= 2.99792458e8  
    h = 6.626068e-34
    k = 1.3806503e-23
    x = (h*nu)/(k*T)

    # Factor of 2 on RHS means this is for 2 polarizations
    brightness = 2.*(h*nu)*(nu/c)**2 * (1./(numpy.exp(x) - 1.))

    return brightness


#-------------------------------------------------
def Brj(nu,T):
    '''
    Rayleigh-Jeans brightness function (2 polarization, in W/m^2/sr/Hz).
    Frequency (nu) must be in Hz.
    Brj(nu,T) = 2.*k*T*(nu/c)**2
    '''

    # Frequency vector must be in Hz.
    # Physical constants in SI units
    c= 2.99792458e8  
    h = 6.626068e-34
    k = 1.3806503e-23
    x = (h*nu)/(k*T)

    # Factor of 2 on RHS means this is for 2 polarizations
    brightness = 2.*k*T*(nu/c)**2

    return brightness


#-------------------------------------------------
def dBnudT(nu,T):
    '''
    Derivative of Bnu(2 polarization, in W/m^2/sr/Hz) with respect to T.
    Frequency (nu) must be in Hz.
    '''

    # Frequency vector must be in Hz.
    # Physical constants in SI units
    c= 2.99792458e8  
    h = 6.626068e-34
    k = 1.3806503e-23
    x = (h*nu)/(k*T)

    # Factor of 2 on RHS means this is for 2 polarizations
    prefac = 2*h**2/(k*c**2)
    expx = numpy.exp(x)
    dBdT = prefac*(nu**4/T**2)*(expx/(expx - 1)**2)

    return dBdT

#-------------------------------------------------
def dBnudTrj(nu,T):
    '''
    Derivative of the Rayleigh Jeans brightness, 
    Brj(2 polarization, in W/m^2/sr/Hz) with respect to T.
    Frequency (nu) must be in Hz.
    '''

    # Frequency vector must be in Hz.
    # Physical constants in SI units
    c= 2.99792458e8  
    h = 6.626068e-34
    k = 1.3806503e-23
    x = (h*nu)/(k*T)

    # Factor of 2 on RHS means this is for 2 polarizations
    dBdT = 2.*k*(nu/c)**2

    return dBdT

