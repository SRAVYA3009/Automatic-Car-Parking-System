The lofty goal for my OpenCV experiment was to take any static image or video of a parking lot and be able to automatically detect whenever a parking space was available or occupied.

Through research and exploration, I discovered how lofty of a goal that was (at least for the scope of a weekend). What I was able accomplish was to detect how many spots were available in a parking lot, with just a bit of upfront work by the user.
To run:
```python
python main.py --image images/parking_lot_1.png --data data/coordinates_1.yml --video videos/parking_lot_1.mp4 --start-frame 400
```
