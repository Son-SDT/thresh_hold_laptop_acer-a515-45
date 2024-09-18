import controller as ctl

fc = ctl.function()
path = f"{fc.get_current_dir()}/autorun.log"

fc.run_cmd(f"rm -r {path}")
fc.run_cmd(f"touch {path}")
