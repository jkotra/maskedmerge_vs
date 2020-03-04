import vapoursynth as vs
import os
import mvsfunc

script_path = os.path.dirname(os.path.abspath(__file__))

core = vs.get_core()
clip_a = core.lsmas.LWLibavSource(script_path + "/GM_clip_1.mkv",threads=6)
clip_b = core.lsmas.LWLibavSource(script_path + "/GM_clip_2.mkv",threads=6)


mask = core.imwri.Read(script_path + "/mask.png",alpha=True)[1]

merged_clip = core.std.MaskedMerge(clip_a,clip_b,mask)
merged_clip.set_output()