import numpy as np
fp = 'Numpy\\MessingWithNumpyFunctions\\Dataset.txt'
data = np.genfromtxt(fp, skip_header=1, usecols=(0,1,2,3))
print(data)
date = data[:,0]
print(date)
t_AVG= data[:,1]
t_MIN = data [:,2]
t_MAX = data [:,3]
print(t_AVG)
print(t_MIN)
print(t_MAX)
date_mask = np.isfinite(date)
# Above is the mdata mask for counting the valid date entries that exist as numbers
print("Number of years:", np.count_nonzero(date_mask))
#Above prints the count returned from the data mask
missing_date_mask = ~np.isfinite(date) 
# Checks for consecutive entries..? Then assignes it to the missing values data mask
print("Number of missing years:", np.count_nonzero(missing_date_mask))
# Counts the number of missing years from the object missing_data_mask
t_AVG_mask = np.isfinite(t_AVG)
print("Number of average temps:", np.count_nonzero(t_AVG_mask))
#Same thing as befores

missing_t_MAX_mask = ~np.isfinite(t_MAX)
print("Number of missing tmax values:", np.count_nonzero(missing_t_MAX_mask))
tmax_mask = np.isfinite(t_MAX)
# Making a mask without the bad values
tmax_clean = t_MAX[tmax_mask]
# Remakign the array with only real values
date_clean = date[tmax_mask]
# Removing corresponding dates
#The tutorial assumes you don't have the t_AVG dataset btw, so we ignore that
tmax_total = tmax_clean[(date_clean >= 1976) & (date_clean <= 2021)]
#New array with the datapoints in that range

print(tmax_total.mean())
#Average of the array
