# aiSquat
## A computer vision solution to track the count of squats
## This tool can be utilized with standard video recordings or in real-time using just a webcam


The barbell squat is a compound, multi-joint exercise intended to target the lumbo-pelvic-hip complex and several lower body muscles (pelvis, low-back, and abdominals). The main joint movements that take place during the squat are as follows:

**Lowering Phase (Eccentric)**
1. Hip flexion
2. Knee flexion
3. Ankle dorsiflexion

**Lifting Phase (Concentric)**

1. Hip extension
2. Knee extension
3. Ankle plantarflexion

To efficiently target these muscles, it is important that a minimum threshold angle is reached between the hip, knee, and ankle, and the code written here quantifies a single squat (100 degrees and less).

Below are two examples where in one a squat is done well, and you can see the count increase in the top left corner, while in the other, the squat is incomplete and the code does not count them as a complete motion. 

### A complete squat
![A complete squat](/results/complete.gif)

### A incomplete squat
![An incomplete squat](/results/incomplete.gif)
