#python

tilt_sum=0
yaw_sum=0
yaw_true=0
def sysCall_init():
    # do some initialization here
    global front_motor, bike, graph,tilt_g, u_g, ref, yaw_g
    front_motor=sim.getObject('../front_motor')
    bike=sim.getObject('../../bike_respondable')
    ref=sim.getObject('../../../../reference_frame')
    """graph=sim.getObject('../../../../Graph')
    tilt_g=sim.addGraphStream(graph,'tilt Angle','rad',0,[1,0,0]);
    yaw_g=sim.addGraphStream(graph,'yaw Angle','rad',0,[0,0,1]);"""
    pass
    
def sysCall_sensing():
    # put your sensing code here
    
    pass

def sysCall_actuation():
    # put your actuation code here
    #tilt=sim.getJointPosition(front_motor)
    #tilt_dot=sim.getJointVelocity(front_motor)
    
    global tilt_sum, tilt_sum, yaw_setpoint, yaw_sum, yaw_true
    yaw_setpoint=sim.getFloatSignal("yaw_setpoint")
    angle=sim.getObjectOrientation(bike,ref);
    vell, vela=sim.getObjectVelocity(bike);
    # tilt angle
    tilt=angle[1];
    tilt_dot=vela[1];
    e_tilt = 0-tilt;
    e_tilt_dot=0-tilt_dot;
    kpt=35
    kdt=-0.00129
    kit=5
    tilt_sum+=e_tilt;
    
    # yaw angle
    yaw=angle[2];
    yaw_dot=vela[2];
    e_yaw = yaw_setpoint-yaw;
    e_yaw_dot=0-yaw_dot;
    yaw_sum+=e_yaw;
    kpy=30
    kiy=0.1
    kdy=5
    u= (-kpt*e_tilt - kdt*e_tilt_dot - kit*tilt_sum) -(-kpy*e_yaw - kdy*e_yaw_dot - kiy*yaw_sum);
    sim.setJointTargetVelocity(front_motor,u);
    """sim.setGraphStreamValue(graph,tilt_g,tilt);
    sim.setGraphStreamValue(graph,yaw_g,yaw);"""
    
        
        
    pass



def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details
