
# %%

!pip install pandas 
!pip install SQLAlchemy

# %%

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://user:user@localhost:6543/user')
df=pd.read_csv('data-1709532629015.csv')
df.to_sql('resource', engine)


# %%
