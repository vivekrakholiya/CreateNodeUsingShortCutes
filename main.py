#tras

 

import hou

 

 

 

#find node path
for node in hou.selectedNodes():
        nodeName = str(node)
        nodePath = node.path()
        newPath = nodePath.replace(nodeName,'')
        nodeInput = node


# middel click in node so yu can seee the node name in '()' and past in 'xform' 
#create transform node
trans = hou.node(str(newPath)).createNode('xform')

 

 

#connect transform input
trans.setNextInput(nodeInput)

 

 

#set display or render flag
trans.setDisplayFlag(1)
trans.setRenderFlag(1)

 

 

#reposition transform node
network = hou.ui.curDesktop().paneTabUnderCursor()
networkPath = network.pwd().path()
pos = network.cursorPosition()
trans.setPosition(pos)
