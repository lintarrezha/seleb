<p align=center><a href="https://linxyz-nine.vercel.app/"> <img src="https://linxyz-nine.vercel.app/favicon.ico"></p> 

## Seleb
Lihat orang-orang yang anda ikuti tapi tidak mengikuti Anda kembali (seleb).

### Requirements (persyaratan)
* [Python3](https://www.python.org/) - Programming Language

### How to Use (cara menggunakan)
1. Download the followers and following data through IG settings. Steps: Setting > Account Center > Your Information and Permission > Download Your Information > Some of your information > Followers and Following✅ > format: JSON > date range: All time (optional) > Download (in current activity). 

2. Clone the repository:
Open your Command Prompt or Terminal
```
git clone https://github.com/lintarrezha/seleb
```

3. Open the repository and create a `data` folder inside:
```
cd seleb
mkdir data
```

4. Place the `followers_1.json` and `following.json` files that you've downloaded from IG settings into the `data` folder.

5. Run the main.py:
```
python main.py
```
or
```
python3 main.py
```