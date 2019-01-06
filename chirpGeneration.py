def chirpGeneration(f1, f2, signalLength, sampleRate, gaussianOn):
    import scipy.signal
    import numpy as np
    import matplotlib.pyplot as plt

    def arrayProduct(a,b):
        c = []
        try:
            for i in range(0, len(a)-1):
                c.append(a[i] * b[i])
            return c
        except:
            return 0
    #EXAMPLE VALUES: 
    #sampleRate = 250*10**6
    #signalLength = 25*10**(-6)
    #f1 = 1.0*10**6
    #f2 = 9.0*10**6
    timeStep = 1.0/sampleRate
    totalNOfSamples = signalLength*1.0/timeStep
    timeVector = np.linspace(0, signalLength, totalNOfSamples)
    chirp = scipy.signal.chirp(timeVector, f1, signalLength, f2, method='linear', phi=0, vertex_zero=True)
    if(gaussianOn == 1):
        window = scipy.signal.gaussian(len(chirp) +1, std=(0.2*len(chirp)))
        chirp = arrayProduct(window,chirp)
    #plt.plot(timeVector, chirp)
    #plt.show()

    return timeVector, chirp
