# Stereo-Camera
1. All the points on projective line to **P** map to **p**
   ![Screenshot 2024-05-19 083950](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/0f8fd5d1-55e8-4247-8277-e6975b266009)

2. All Points on projective line to P in left camera map to a line in the image plane of the right camera
   ![Screenshot 2024-05-19 084355](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/98a4f724-53e4-4bd4-8147-c98cac28e919)

3. If i search this line to find correspondances..
   ![Screenshot 2024-05-19 084450](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/9a7e1e2f-abd4-4b53-bf41-671434b86d1f)
4. I can get 3D!
   ![Screenshot 2024-05-19 084539](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/e52a0999-58f8-4e6e-acfd-f67688d2eee0)

5. **Stereo**
   ![Screenshot 2024-05-19 084614](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/552fda44-aae3-40c1-abaa-7b20818dbc13)
6. **Parallel Calibrated Cameras**
   - We Assume that the two calibrated cameras (we know instrics and exterinsics ) are parallel, i.e. the right camera is just some distance 
     to the right of the left camera. We assume we know this distance. We 
     call it the baseline.
     ![Screenshot 2024-05-19 085304](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/46f70c9f-4bf8-4e41-9109-c65a82e5ab70)


  - Pick a point P in the world.
    ![Screenshot 2024-05-19 085448](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/db595e54-0686-49dd-9244-7fde517f9805)


    - Points O[l], O[r] and P (and p[i] and p[r]) lie on a plane. Sice two image planes lie on the same plane (distance f from each camera), the lines O[i]O[r] and p[i]p[r] are parallel.
      ![Screenshot 2024-05-19 085922](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/e080d32c-8553-4db5-b11f-fc2794b49f40)


  - Since lines O[l]O[r] and p[l]p[r] are parallel, and O[l] and O[r] have the same y, then also p[l] and p[r] have the same y: y[r] = y[l].
    ![Screenshot 2024-05-19 090158](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/916d0301-5157-43a6-bbbb-264568c75e6a)

    - Since our points p[l] and p[r] lie on a horizontal line, we can forget about y[l] for a moment(it does not seem important). Let's look at the camera situation from the birdeye perspective instead. Let's see if we can find a connection between x[l], x[r] and Z(because Z is what we want).
      ![Screenshot 2024-05-19 090742](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/4347c25b-044d-48ec-af00-a0b2c216b88e)

    - We can then use similar triangles to compute the depth of a point P
      ![Screenshot 2024-05-19 090848](https://github.com/Tapan2903patel/Stereo-Camera/assets/112714790/947ab563-fd59-4cd2-a05a-08a8c3be079e)

      




