# -*- coding: utf-8 -*-

import numpy as nup

class Mesh:
    def __init__(self):
        None
    def combineMesh(self,ob1,ob2):
        # Check for largest mesh
        if (ob1.nf < ob2.nf):
            coinTest = ob1.makeCoin()
            coinTarg = ob2.makeCoin()
        else:
            coinTest = ob2.makeCoin()
            coinTarg = ob1.makeCoin()
        # Check for duplicate panels
        delList = []
        for iF in range(nup.size(coinTest[1,1,:])):
            panelTest = coinTest[:,:,iF]
            for iFF in range(nup.size(coinTarg[1,1,:])):
                panelTarg = coinTarg[:,:,iFF]
                isEq = nup.sum(panelTest==panelTarg)
                if (isEq == 12):
                    coinTarg = nup.delete(coinTarg,iFF,2)
                    delList.append(iF)
        coinTest = nup.delete(coinTest,delList,2)
        # Concatenate unique meshes
        coin = nup.concatenate((coinTest,coinTarg),axis=2)
        self.np = nup.size(coin[1,1,:])*4
        self.nf = nup.size(coin[1,1,:])
        self.X = nup.zeros(nup.size(coin[1,1,:])*4)
        self.Y = nup.zeros(nup.size(coin[1,1,:])*4)
        self.Z = nup.zeros(nup.size(coin[1,1,:])*4)
        self.P = nup.zeros((nup.size(coin[1,1,:]),4),dtype = int)

        iP = 0
        for iF in range(nup.size(coin[1,1,:])):
            for iC in range(4):
                self.X[iP] = coin[0,iC,iF]
                self.Y[iP] = coin[1,iC,iF]
                self.Z[iP] = coin[2,iC,iF]
                iP += 1
            self.P[iF,0] = 1+(iF)*4
            self.P[iF,1] = 2+(iF)*4
            self.P[iF,2] = 3+(iF)*4
            self.P[iF,3] = 4+(iF)*4
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin
    def delHorPan(self):
        coin = self.makeCoin()
        apex = nup.min(self.Z)
        zLoc = nup.zeros(4)
        delList = []
        # Check every panel for horizontality and higher position than lowest point
        for iP in range(self.nf):
            for iC in range(4):
                zLoc[iC] = coin[2,iC,iP]
            if (nup.abs(nup.mean(zLoc)-zLoc[0]) < 0.001 and nup.mean(zLoc) > apex):
                delList.append(iP)
        # Delete selected panels
        coin = nup.delete(coin,delList,2)
        # Remake mesh
        self.np = nup.size(coin[1,1,:])*4
        self.nf = nup.size(coin[1,1,:])
        self.X = nup.zeros(nup.size(coin[1,1,:])*4)
        self.Y = nup.zeros(nup.size(coin[1,1,:])*4)
        self.Z = nup.zeros(nup.size(coin[1,1,:])*4)
        self.P = nup.zeros((nup.size(coin[1,1,:]),4),dtype = int)

        iP = 0
        for iF in range(nup.size(coin[1,1,:])):
            for iC in range(4):
                self.X[iP] = coin[0,iC,iF]
                self.Y[iP] = coin[1,iC,iF]
                self.Z[iP] = coin[2,iC,iF]
                iP += 1
            self.P[iF,0] = 1+(iF)*4
            self.P[iF,1] = 2+(iF)*4
            self.P[iF,2] = 3+(iF)*4
            self.P[iF,3] = 4+(iF)*4
        
def writeMesh(msh,filename):
    with open(filename,'w') as f:
        f.write('{:d}\n'.format(msh.np))
        f.write('{:d}\n'.format(msh.nf))
        for iP in range(msh.np):
            f.write('  {:.7f}  {:.7f}  {:.7f}\n'.format(msh.X[iP],msh.Y[iP],msh.Z[iP]))
        for iF in range(msh.nf):
            f.write('  {:d}  {:d}  {:d}  {:d}\n'.format(msh.P[iF,0],msh.P[iF,1],msh.P[iF,2],msh.P[iF,3]))
        return None

class box:
    def __init__(self,length,width,height,cCor):
        self.length = length
        self.width = width
        self.height = height
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'box'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)
    def panelize(self):
        self.nf = 6
        self.np = 8
        self.X = nup.array([-self.length/2.0,self.length/2.0,-self.length/2.0,self.length/2.0,-self.length/2.0,self.length/2.0,-self.length/2.0,self.length/2.0])
        self.Y = nup.array([self.width/2.0,self.width/2.0,self.width/2.0,self.width/2.0,-self.width/2.0,-self.width/2.0,-self.width/2.0,-self.width/2.0])
        self.Z = nup.array([-self.height/2.0,-self.height/2.0,self.height/2.0,self.height/2.0,-self.height/2.0,-self.height/2.0,self.height/2.0,self.height/2.0])     
        self.P = nup.zeros([6,4],dtype = int)
        self.P[0,:] = nup.array([3,4,2,1])
        self.P[1,:] = nup.array([4,8,6,2])
        self.P[2,:] = nup.array([8,7,5,6])
        self.P[3,:] = nup.array([7,3,1,5])
        self.P[4,:] = nup.array([2,6,5,1])
        self.P[5,:] = nup.array([8,4,3,7])
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2

    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin
        
class cone:
    def __init__(self,diameter,height,cCor):
        self.diameter = diameter
        self.height = height
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'cone'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)

    def panelize(self):
        Ntheta = 18
        Nz = 3
        theta = [xx*2*nup.pi/(Ntheta-1) for xx in range(Ntheta)]        
        self.nf = 0
        self.np = 0
        r = [0,self.diameter/2.0,0]
        z = [0,0,-self.height]
        self.X = []
        self.Y = []
        self.Z = []
        self.P = nup.zeros([(len(r)-1)*(Ntheta-1),4],dtype = int)
        n = len(r)
        
        for iT in range(Ntheta):
            for iN in range(n):
                self.X.append(r[iN]*nup.cos(theta[iT])) 
                self.Y.append(r[iN]*nup.sin(theta[iT]))
                self.Z.append(z[iN])
                self.np += 1
        
        iP = 0
        for iN in range(1,n):
            for iT in range(1,Ntheta):
                self.P[iP,0] = iN + n*(iT-1)
                self.P[iP,1] = iN + 1 + n*(iT-1)
                self.P[iP,2] = iN + 1 + n*iT
                self.P[iP,3] = iN + n*iT
                self.nf += 1
                iP += 1
                
        self.X = nup.array(self.X)
        self.Y = nup.array(self.Y)
        self.Z = nup.array(self.Z)
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
            
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin
                
class cylinder:
    def __init__(self,diameter,height,cCor):
        self.diameter = diameter
        self.height = height
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'cylinder'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)

    def panelize(self):
        Ntheta = 18
        Nz = 3
        theta = [xx*2*nup.pi/(Ntheta-1) for xx in range(Ntheta)]        
        self.nf = 0
        self.np = 0
        r = [0,self.diameter/2.0,self.diameter/2.0,0]
        z = [0,0,-self.height,-self.height]
        self.X = []
        self.Y = []
        self.Z = []
        self.P = nup.zeros([(len(r)-1)*(Ntheta-1),4],dtype = int)
        n = len(r)
        
        for iT in range(Ntheta):
            for iN in range(n):
                self.X.append(r[iN]*nup.cos(theta[iT])) 
                self.Y.append(r[iN]*nup.sin(theta[iT]))
                self.Z.append(z[iN])
                self.np += 1
        
        iP = 0
        for iN in range(1,n):
            for iT in range(1,Ntheta):
                self.P[iP,0] = iN + n*(iT-1)
                self.P[iP,1] = iN + 1 + n*(iT-1)
                self.P[iP,2] = iN + 1 + n*iT
                self.P[iP,3] = iN + n*iT
                self.nf += 1
                iP += 1
                
        self.X = nup.array(self.X)
        self.Y = nup.array(self.Y)
        self.Z = nup.array(self.Z)
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
        
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin

class hemicylinder:
    def __init__(self,diameter,height,cCor):
        self.diameter = diameter
        self.height = height
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'hemicylinder'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)

    def panelize(self):
        Ntheta = 18
        Nz = 3
        theta = [xx*nup.pi/(Ntheta-1)-nup.pi/2.0 for xx in range(Ntheta)]        
        self.nf = 0
        self.np = 0
        r = [0,self.diameter/2.0,self.diameter/2.0,0]
        z = [self.height/2.0,self.height/2.0,-self.height/2.0,-self.height/2.0]
        self.X = []
        self.Y = []
        self.Z = []
        self.P = nup.zeros([(len(r)-1)*(Ntheta-1),4],dtype = int)
        n = len(r)
        
        for iT in range(Ntheta):
            for iN in range(n):
                self.Z.append(-r[iN]*nup.cos(theta[iT])) 
                self.X.append(r[iN]*nup.sin(theta[iT]))
                self.Y.append(z[iN])
                self.np += 1
        
        iP = 0
        for iN in range(1,n):
            for iT in range(1,Ntheta):
                self.P[iP,3] = iN + n*(iT-1)
                self.P[iP,2] = iN + 1 + n*(iT-1)
                self.P[iP,1] = iN + 1 + n*iT
                self.P[iP,0] = iN + n*iT
                self.nf += 1
                iP += 1
                
        self.X = nup.array(self.X)
        self.Y = nup.array(self.Y)
        self.Z = nup.array(self.Z)
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
        
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin

class sphere:
    def __init__(self,diameter,cCor):
        self.diameter = diameter
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'sphere'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)
        
    def panelize(self):
        Ntheta = 18
        Nz = 3
        theta = [xx*2*nup.pi/(Ntheta-1) for xx in range(Ntheta)]
        phi = [xx*nup.pi/(Ntheta/2-1) for xx in range(Ntheta/2)]        
        self.nf = 0
        self.np = 0
        r = self.diameter/2.0
        self.X = []
        self.Y = []
        self.Z = []
        self.P = nup.zeros([(Ntheta-1)*(Ntheta/2-1),4],dtype = int)
        
        for iT in range(Ntheta/2):
            for iTT in range(Ntheta):
                self.X.append(r*nup.cos(theta[iTT])*nup.sin(phi[iT])) 
                self.Y.append(r*nup.sin(theta[iTT])*nup.sin(phi[iT]))
                self.Z.append(r*nup.cos(phi[iT]))
                self.np += 1
        
        iP = 0
        for iN in range(1,Ntheta):
            for iT in range(1,Ntheta/2):
                self.P[iP,3] = iN + Ntheta*(iT-1)
                self.P[iP,2] = iN + 1 + Ntheta*(iT-1)
                self.P[iP,1] = iN + 1 + Ntheta*iT
                self.P[iP,0] = iN + Ntheta*iT
                self.nf += 1
                iP += 1
        self.X = nup.array(self.X)
        self.Y = nup.array(self.Y)
        self.Z = nup.array(self.Z)
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
        
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin

class hemisphere:
    def __init__(self,diameter,cCor):
        self.diameter = diameter
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'hemisphere'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)

    def panelize(self):
        Ntheta = 18
        theta = [xx*2*nup.pi/(Ntheta-1) for xx in range(Ntheta)]
        phi = [xx*nup.pi/2.0/(Ntheta/2-1) for xx in range(Ntheta/2)]        
        self.nf = 0
        self.np = 0
        r = self.diameter/2.0
        self.X = []
        self.Y = []
        self.Z = []
        self.P = nup.zeros([(Ntheta-1)*(Ntheta/2-1),4],dtype = int)
        
        for iT in range(Ntheta/2):
            for iTT in range(Ntheta):
                self.X.append(r*nup.cos(theta[iTT])*nup.sin(phi[iT])) 
                self.Y.append(r*nup.sin(theta[iTT])*nup.sin(phi[iT]))
                self.Z.append(-r*nup.cos(phi[iT]))
                self.np += 1
        
        iP = 0
        for iN in range(1,Ntheta):
            for iT in range(1,Ntheta/2):
                self.P[iP,0] = iN + Ntheta*(iT-1)
                self.P[iP,1] = iN + 1 + Ntheta*(iT-1)
                self.P[iP,2] = iN + 1 + Ntheta*iT
                self.P[iP,3] = iN + Ntheta*iT
                self.nf += 1
                iP += 1
                
        self.X = nup.array(self.X)
        self.Y = nup.array(self.Y)
        self.Z = nup.array(self.Z)
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
        
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin

class wedge:
    def __init__(self,length,width,height,cCor):
        self.length = length
        self.width = width
        self.height = height
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'wedge'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)
    def panelize(self):
        self.nf = 6
        self.np = 8
        self.X = nup.array([0.0,0.0,-self.length/2.0,self.length/2.0,0.0,0.0,-self.length/2.0,self.length/2.0])
        self.Y = nup.array([self.width/2.0,self.width/2.0,self.width/2.0,self.width/2.0,-self.width/2.0,-self.width/2.0,-self.width/2.0,-self.width/2.0])
        self.Z = nup.array([-self.height,-self.height,0.0,0.0,-self.height,-self.height,0.0,0.0])     
        self.P = nup.zeros([6,4],dtype = int)
        self.P[0,:] = nup.array([3,4,2,1])
        self.P[1,:] = nup.array([4,8,6,2])
        self.P[2,:] = nup.array([8,7,5,6])
        self.P[3,:] = nup.array([7,3,1,5])
        self.P[4,:] = nup.array([2,6,5,1])
        self.P[5,:] = nup.array([8,4,3,7])
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
        
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin

class pyramid:
    def __init__(self,length,width,height,cCor):
        self.length = length
        self.width = width
        self.height = height
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'pyramid'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)
    def panelize(self):
        self.nf = 6
        self.np = 8
        self.X = nup.array([0.0,0.0,-self.length/2.0,self.length/2.0,0.0,0.0,-self.length/2.0,self.length/2.0])
        self.Y = nup.array([0.0,0.0,self.width/2.0,self.width/2.0,0.0,0.0,-self.width/2.0,-self.width/2.0])
        self.Z = nup.array([-self.height,-self.height,0.0,0.0,-self.height,-self.height,0.0,0.0])     
        self.P = nup.zeros([6,4],dtype = int)
        self.P[0,:] = nup.array([3,4,2,1])
        self.P[1,:] = nup.array([4,8,6,2])
        self.P[2,:] = nup.array([8,7,5,6])
        self.P[3,:] = nup.array([7,3,1,5])
        self.P[4,:] = nup.array([5,6,5,1])
        self.P[5,:] = nup.array([8,4,3,7])
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
        
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin

class torus:
    def __init__(self,diamOut,diamIn,cCor):
        self.diamOut = diamOut
        self.diamIn = diamIn
        self.xC = cCor[0]
        self.yC = cCor[1]
        self.zC = cCor[2]
        self.name = 'torus'
        self.panelize()
        self.translate(self.xC,self.yC,self.zC)

    def panelize(self):
        Ntheta = 18
        Nphi = 18
        theta = [xx*2*nup.pi/(Ntheta-1) for xx in range(Ntheta)]
        phi = [xx*2*nup.pi/(Nphi-1) for xx in range(Nphi)]                
        self.nf = 0
        self.np = 0
        self.X = []
        self.Y = []
        self.Z = []
        R = self.diamOut
        r = self.diamIn
        
        for iT in range(Ntheta):
            for iP in range(Nphi):
                self.X.append((R+r*nup.cos(theta[iT]))*nup.cos(phi[iP])) 
                self.Y.append((R+r*nup.cos(theta[iT]))*nup.sin(phi[iP]))
                self.Z.append(r*nup.sin(theta[iT]))
                self.np += 1
        
        self.nf = (Ntheta-1)*(Nphi-1)
        self.P = nup.zeros([self.nf,4],dtype = int)
        iPan = 0
        for iT in range(Ntheta-1):
            for iP in range(Nphi-1):
                self.P[iPan,0] = iP +iT*Nphi + 1 
                self.P[iPan,1] = iP+1 +iT*Nphi + 1
                self.P[iPan,2] = iP+1+Ntheta +iT*Nphi + 1
                self.P[iPan,3] = iP+Ntheta +iT*Nphi + 1
                iPan += 1
                
        self.X = nup.array(self.X)
        self.Y = nup.array(self.Y)
        self.Z = nup.array(self.Z)
        # Define triangles for plotting
        self.trii = nup.zeros([2*self.nf,3],dtype = int)
        iT = 0
        for iTr in range(self.nf):
            self.trii[iT,:] = [self.P[iTr,0]-1,self.P[iTr,1]-1,self.P[iTr,2]-1]
            self.trii[iT+1,:] = [self.P[iTr,0]-1,self.P[iTr,2]-1,self.P[iTr,3]-1]
            iT += 2
            
    def translate(self,xT,yT,zT):
        self.X += xT
        self.Y += yT
        self.Z += zT
    def rotate(self,a1,a2,theta):
        R = nup.zeros([3,3])
        # Normal vector through origin
        u = a2[0] - a1[0]        
        v = a2[1] - a1[1]        
        w = a2[2] - a1[2]
        u = u/nup.sqrt(u**2+v**2+w**2)        
        v = v/nup.sqrt(u**2+v**2+w**2)        
        w = w/nup.sqrt(u**2+v**2+w**2)        
        # Translate mesh so that rotation axis starts from the origin
        self.X -= a1[0]
        self.Y -= a1[1]
        self.Z -= a1[2]
        
        # Rotation matrix
        R[0,0] = u**2 + nup.cos(theta)*(1 - u**2)
        R[0,1] = u*v*(1-nup.cos(theta)) - w*nup.sin(theta)
        R[0,2] = u*w*(1-nup.cos(theta)) + v*nup.sin(theta)
        R[1,0] = u*v*(1-nup.cos(theta)) +w*nup.sin(theta)
        R[1,1] = v**2 + nup.cos(theta)*(1-v**2)
        R[1,2] = v*w*(1-nup.cos(theta)) - u*nup.sin(theta)
        R[2,0] = w*u*(1-nup.cos(theta)) - v*nup.sin(theta)
        R[2,1] = w*v*(1-nup.cos(theta)) + u*nup.sin(theta)
        R[2,2] = w**2 + nup.cos(theta)*(1-w**2)
        
        for iP in range(self.np):
            p1 = nup.array([self.X[iP],self.Y[iP],self.Z[iP]])
            p2 = nup.dot(R,p1)
            self.X[iP] = p2[0]
            self.Y[iP] = p2[1]
            self.Z[iP] = p2[2]

        # Translate back to original position
        
        self.X += a1[0]
        self.Y += a1[1]
        self.Z += a1[2]
    def makeCoin(self):
        coin = nup.zeros((3,4,self.nf))
        for iF in range(self.nf):
            for iC in range(4):
                coin[0,iC,iF] = self.X[self.P[iF,iC]-1]
                coin[1,iC,iF] = self.Y[self.P[iF,iC]-1]
                coin[2,iC,iF] = self.Z[self.P[iF,iC]-1]
        return coin