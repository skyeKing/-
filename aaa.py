import maya.cmds as cmds
import maya.mel as mel
import logging
'''
#ע�⣺���ܳ���˫��ref��ѡ�е�������������в�ͬ�������ռ䣨ǰ׺��
'''
moCapDataFrom = [u'Root_M', u'Hip_R', u'Knee_R', u'Ankle_R', u'Toes_R', u'ToesEnd_R', 
                 u'Spine1_M', u'Spine1Part1_M', u'Chest_M', u'Scapula_R', u'Shoulder_R', u'Elbow_R', 
                 u'Wrist_R', u'MiddleFinger1_R', u'MiddleFinger2_R', u'MiddleFinger3_R', 
                 u'MiddleFinger4_R', u'ThumbFinger1_R', u'ThumbFinger2_R', u'ThumbFinger3_R', 
                 u'ThumbFinger4_R', u'IndexFinger1_R', u'IndexFinger2_R', u'IndexFinger3_R', 
                 u'IndexFinger4_R', u'Cup_R', u'PinkyFinger1_R', u'PinkyFinger2_R', 
                 u'PinkyFinger3_R', u'PinkyFinger4_R', u'RingFinger1_R', u'RingFinger2_R', 
                 u'RingFinger3_R', u'RingFinger4_R', u'Neck_M', u'NeckPart1_M', u'Head_M', 
                 u'HeadEnd_M', u'Scapula_L', u'Shoulder_L', u'Elbow_L', 
                 u'Wrist_L', u'MiddleFinger1_L', u'MiddleFinger2_L', u'MiddleFinger3_L', 
                 u'MiddleFinger4_L', u'ThumbFinger1_L', u'ThumbFinger2_L', u'ThumbFinger3_L', 
                 u'ThumbFinger4_L', u'IndexFinger1_L', u'IndexFinger2_L', u'IndexFinger3_L', 
                 u'IndexFinger4_L', u'Cup_L', u'PinkyFinger1_L', u'PinkyFinger2_L', u'PinkyFinger3_L', 
                 u'PinkyFinger4_L', u'RingFinger1_L', u'RingFinger2_L', u'RingFinger3_L', u'RingFinger4_L', 
                 u'Hip_L', u'Knee_L', u'Ankle_L', u'Toes_L', u'ToesEnd_L']

fkikSwitchList = ['FKIK%s'%ctl for ctl in ['Arm_L','Arm_R','Spine_M','Leg_L','Leg_R ']]

sel = cmds.ls(sl=1)
if len(sel) < 2 :logging.warn(u'��ѡ���������壬��ѡ��DK����������һ�����壬��ѡ����������ڵ�ref������һ�����壬�㵱ǰѡ����%s��'%len(sel))
elif len(sel) > 2:logging.warn(u'��ѡ���������壬��ѡ��DK����������һ�����壬��ѡ����������ڵ�ref������һ�����壬�㵱ǰѡ����%s��'%len(sel))
else:
    fromObject,toObject = sel
    countChar = 0
    #���� ѡ�е�������û��˫��REF������
    for ii in sel:
        if ':' in ii:
            countChar += 1
    if not countChar:logging.warn(u'��ѡ�е��������嶼�����з��š�:�����޷�ʶ������������ռ������')
    else:
        nsA,ObjA = fromObject.split(':')
        nsB,ObjB = toObject.split(':')
        if nsA == nsB:logging.warn(u'��ѡ����ͬһ�����ϵĶ���')
        else:
            for eachSwitch in fkikSwitchList:
                if cmds.objExists('%s:%s'%(nsB,eachSwitch)) and cmds.objExists('%s:%s.FKIKBlend'%(nsB,eachSwitch)):
                    cmds.setAttr('%s:%s.FKIKBlend'%(nsB,eachSwitch),0)
                                
            cmds.select([ '%s:%s'%(nsA,ctl) for ctl in moCapDataFrom if cmds.objExists('%s:%s'%(nsA,ctl))],r=1)
            cmds.setKeyframe(at='rx',t=-20,v=0)
            cmds.setKeyframe(at='ry',t=-20,v=0)
            cmds.setKeyframe(at='rz',t=-20,v=0)
            cmds.select(cl=1)
            cmds.currentTime(-20)
            
            #cmds.currentTime(0)
            cmds.select('%s:FKRoot_M'%nsB,'%s:Root_M'%nsA,r=1)
            pC = cmds.parentConstraint(w=1,mo=0)
            cmds.setKeyframe(at='tx',t=-20)
            cmds.setKeyframe(at='ty',t=-20)
            cmds.setKeyframe(at='tz',t=-20) 
            cmds.setKeyframe(at='rx',t=-20,v=0)
            cmds.setKeyframe(at='ry',t=-20,v=0)
            cmds.setKeyframe(at='rz',t=-20,v=0)
            cmds.delete(pC)
            
            addConsList = []
            for eachCtl in moCapDataFrom:
                jointName , ctlName = '%s:%s'%(nsA,eachCtl),'%s:FK%s'%(nsB,eachCtl)
                if cmds.objExists(jointName) and cmds.objExists(ctlName):
                    if not 'Root' in eachCtl:
                        tempCons = cmds.orientConstraint(jointName,ctlName,w=1,mo=1)
                    else:
                        tempCons = cmds.parentConstraint(jointName,ctlName,w=1,mo=0)
                    addConsList.extend(tempCons)
                else:
                    if not cmds.objExists(jointName):logging.info(u'������%s'%jointName)
                    elif not cmds.objExists(ctlName):logging.info(u'������%s'%ctlName)
                        
            
            
                 