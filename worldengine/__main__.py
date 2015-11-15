import os
import sys
import numpy
import worldengine
from worldengine.plates import world_gen
from worldengine.world import World
from worldengine.draw import draw_ancientmap_on_file

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

    # parameters
    seed = 1017
    width = 784
    height = 512
    output_dir = "../../worldengine_profiled_worlds"
    generation = len(sys.argv) == 1  # if any parameter is given, create an ancien map instead

    # start work
    if generation:
        print("Profiling of world-generation started, seed = %s" % (seed))
    else:
        print("Profiling of ancient map-generation started, seed = %s" % (seed))
    print("")

    worldname = "seed_%i" % seed
    numpy.random.seed(seed)

    if generation:  # generate world
        w = world_gen(worldname, width, height, seed)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        w.protobuf_to_file("%s/%s.world" % (output_dir, worldname))
    else:  # draw ancient map
        w = World.open_protobuf("%s/%s.world" % (output_dir, worldname))
        draw_ancientmap_on_file(w, "%s/ancientmap.png" % (output_dir), resize_factor=3)
