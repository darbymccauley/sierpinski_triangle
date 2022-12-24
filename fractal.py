import numpy as np
import matplotlib.pyplot as plt
import time

class Triangle:
    def __init__(self):
        """
        Define and instantiate base equilateral triangle characteristics.
        """
        self.offset = 5 # x coord where left-most point begins
        self.length = 10 # length of sides
        self.height = (np.sqrt(3)/2)*self.length 
        self.half_length_x_coord = self.length/2 + self.offset

    def base_triangle(self):
        """
        Creates the outer equilateral triangle.
        Returns the coordinates of its verticies.
        """
        x_coords = [self.offset, self.offset+self.length, self.half_length_x_coord]
        y_coords = [self.offset, self.offset, self.height]
        return x_coords, y_coords

    def choose_vertex(self):
        """
        Choose a vertex at random and return it's coordinates.
        """
        xs_verticies, ys_verticies = self.base_triangle()
        N = np.random.randint(0, 3)
        assert(N < 3)
        assert(N >= 0)
        if N == 0:
            return xs_verticies[0], ys_verticies[0]
        elif N == 1:
            return xs_verticies[1], ys_verticies[1]
        elif N == 2:
            return xs_verticies[2], ys_verticies[2]


    def random_pnt_within_triangle(self):
        """
        Generate a point within the outer triangle and return
        its coordinates.
        """
        # Define the verticies, which service as bounds for where a random
        # point can generate from/within
        xs_verticies, ys_verticies = self.base_triangle()
        pnt0 = (xs_verticies[0], ys_verticies[0])
        pnt1 = (xs_verticies[1], ys_verticies[1])
        pnt2 = (xs_verticies[2], ys_verticies[2])
        
        x, y = sorted([np.random.random(), np.random.random()])
        a, b, c = x, y-x, 1-y
        random_x = a*pnt0[0] + b*pnt1[0] + c*pnt2[0]
        random_y = a*pnt1[1] + b*pnt1[1] + c*pnt2[1]
        return random_x, random_y

    def new_position(self, vertex_coords, cur_pos):
        """
        Compute the half distance between the vertex and random
        point and return the computed points coordinates.
        """
        x_diff_half = (vertex_coords[0] - cur_pos[0])/2
        y_diff_half = (vertex_coords[1] - cur_pos[1])/2
        new_pos = cur_pos[0]+x_diff_half, cur_pos[1]+y_diff_half
        return new_pos


    def run(self, N=10000):
        """
        Run the fractal.
        """
        xs_verticies, ys_verticies = self.base_triangle()
        xs_verticies.append(self.offset), ys_verticies.append(self.offset)
        plt.ion()
        fig = plt.figure()
        plt.plot(xs_verticies, ys_verticies, 'k-', zorder=10) # plot outer triangle
        cur_pos = self.random_pnt_within_triangle()
        plt.plot(*cur_pos, c="C0", marker="o", markersize=5, zorder=2)
        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        cur_vert = self.choose_vertex()
        for n in range(N):
            new_pos = self.new_position(cur_vert, cur_pos)
            plt.plot(*new_pos, c="C0", marker="o", markersize=5, zorder=2)
            fig.canvas.draw_idle()
            fig.canvas.flush_events()
            time.sleep(0.01)
            cur_pos = new_pos
            cur_vert = self.choose_vertex() # choose new vertex point
        plt.ioff()
        plt.show()


if __name__=="__main__":
    t = Triangle()
    t.run()
