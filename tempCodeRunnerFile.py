
num_mels = 128
num_chroma = 12
num_mfcc = 13

num_features = num_mfcc + num_mels + num_chroma * 3 + 3  # 3 for zcr, spectral_centroid, flatness

