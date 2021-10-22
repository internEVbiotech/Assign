#Description at the very end.From line 33.
#importing the biosteam library
import biosteam as bst
# getting the chemicals we are going to use
bst.settings.set_thermo(['Water','Ethanol', 'Octane'])
#defining each stream , with the wanted concentration
s1=bst.Stream('s1', Water= 100)
s2=bst.Stream('s2', Ethanol= 50)
s3=bst.Stream('s3', Octane= 20)
#effluent and recycle will be calculated by the splitter
recycle = bst.Stream('recycle')
effluent = bst.Stream('effluent')
#Making a unit, hence a class (object constructor) should be formed so we can 'call' it later in the code. Here we are doing a mixing, with 3 inputes and only one output
#from biosteam import Unit, then this command could be Mixer(Unit)
class Mixer(bst.Unit):
    _N_outs = 1
    _N_ins = 3
#with _run command: Run simulation and update output streams.
    def _run(self):
        s_out, = self.outs #took this command from the biosteam. Do not know why there is a comma(without it doesn't work)
        s_out.mix_from(self.ins)


U1 = Mixer('U1', ins=[s1,s2, s3], outs='')

P1 = bst.Pump('P1', U1-0)
S1 = bst.Splitter('S1', P1-0, outs=('effluent', 'recycle'), split=0.9)


system_assign = bst.System('manual_sys', path=[U1, P1, S1], recycle=recycle)
system_assign.simulate()
system_assign.show()

#Previous week and Wednesday I got very stuck of what kind of process. But since the meeting on tuesday. I decided to make a process with no actual end goal
#This is why I decided to mix 3 different streams. With a unit created by me. I removed some commands
# Later on I used 2 default units from BIOSTEAM, from which one, the Splitter,
#has a recycle stream from the splitter to the mixer.

