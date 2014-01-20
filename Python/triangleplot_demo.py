'''Draws three triangle-axis plots; two are soil plots, one not. CPHLewis, UCBerkeley, 2008-2012.'''
from matplotlib import use
use('Agg') # This is a graphics backend; you might prefer another one
from Ternary import TernaryPlot
import matplotlib.cm as cm

CZnSn = TernaryPlot('Cu Zn Sn')
CZnSn.axistitles(labelnames=['Cu','Sn','Zn'])
CZnSn.line([25,75,0],[0,0,100])
CZnSn.line([45,55,0],[0,0,100])
CZnSn.show('triangleplot_CuZnSn298')

CZnS = TernaryPlot('Cu Zn S')
CZnS.axistitles(labelnames=['Cu','Zn','S'])
CZnS.line([0,100,0],[50,0,50])
#Right
CZnS.line([50,50,0],[50,0,50])
CZnS.line([58.5,41.5,0],[50,0,50])
CZnS.line([52,48,0],[50,0,50])
CZnS.line([61.5,38.5,0],[50,0,50])
#Left
CZnS.line([0,64,36],[50,0,50])
CZnS.line([0,66,34],[50,0,50])
CZnS.line([0,66.5,33.5],[50,0,50])
CZnS.line([0,65.5,34.5],[50,0,50])
CZnS.line([0,50,50],[50,0,50])
CZnS.show('triangleplot_CuZnS298')

ZnSnS = TernaryPlot('Zn Sn S')
ZnSnS.axistitles(labelnames=['S','Zn','Sn'])
ZnSnS.line([50,50,0],[0,50,50])
ZnSnS.line([50,50,0],[0,60,40])
ZnSnS.line([50,50,0],[0,66,34])
ZnSnS.line([50,50,0],[0,0,100])
ZnSnS.show('triangleplot_ZnSnS298')

ZnSnS = TernaryPlot('Zn Sn S')
ZnSnS.axistitles(labelnames=['S','Zn','Sn'])
ZnSnS.line([50,50,0],[0,50,50])
ZnSnS.line([50,50,0],[0,60,40])
ZnSnS.line([50,50,0],[0,66,34])
ZnSnS.line([50,50,0],[0,0,100])
ZnSnS.line([100,0,0],[0,50,50])
ZnSnS.line([100,0,0],[0,60,40])
ZnSnS.line([100,0,0],[0,66,34])
ZnSnS.show('triangleplot_ZnSnS298-before')

CSnS = TernaryPlot('Cu S Sn')
CSnS.axistitles(labelnames=['Cu','S','Sn'])
CSnS.line([34,66,0],[60,0,40])
CSnS.line([0,55,45],[50,0,50])
CSnS.line([0,75,25],[50,0,50])
CSnS.line([0,100,0],[50,0,50])
CSnS.line([34,66,0],[50,0,50])
CSnS.line([50,50,0],[66.7,0,33.3])
CSnS.line([36,64,0],[66.7,0,33.3])
CSnS.line([34,66,0],[66.7,0,33.3])
CSnS.line([34.5,65.5,0],[66.7,0,33.3])
CSnS.line([33.5,66.5,0],[66.7,0,33.3])
CSnS.show('triangleplot_CuSnS298')

					
