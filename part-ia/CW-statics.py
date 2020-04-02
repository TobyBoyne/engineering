import matplotlib.pyplot as plt
import numpy as np

class Joint:
	def __init__(self, x, y, support=False, load=False):
		self.x = x
		self.y = y
		self.members = []

	def get_pos(self):
		return self.x, self.y

	def add_member(self, member):
		self.members.append(member)

	def angle_of_member(self, member):
		return member.get_angle(self)

	def draw(self):
		plt.plot(self.x, self.y, 'o')


class Member:
	def __init__(self, joint1, joint2):
		self.joints = (joint1, joint2)
		for j in joints:
			j.add_member(self)


	def get_angle(self, start_joint):
		start, end = sorted(self.joints, key=lambda x: x is start_joint, reverse=True)
		dy, dx = (p2 - p1 for (p1, p2) in zip(start.get_pos(), end.get_pos()))
		# clockwise angle between vertical and member
		return np.arctan2(dy, dx)

	def draw(self):
		xs, ys = zip(*map(lambda j: j.get_pos(), self.joints))
		plt.plot(xs, ys)


fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.autoscale(False)




def onclick(event):
	pass
	# print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
	# 	  (event.button, event.x, event.y, event.xdata, event.ydata))
	#
	# plt.plot(event.xdata, event.ydata, 'x')
	#
	# fig.canvas.draw()


def onmove(event):
	pass



events = (
	fig.canvas.mpl_connect('button_press_event', onclick),
	fig.canvas.mpl_connect('motion_notify_event', onmove)
)

joints = [
	Joint(2, 2),
	Joint(10, 3),
	Joint(4, 2),
	Joint(4, 4)
]

members = [
	Member(joints[0], joints[1])
]

for item in joints + members:
	item.draw()


plt.show()