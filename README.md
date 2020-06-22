#Quick Start


provides
```python



class SlurmCharm(CharmBase):
    _state = StoredState()
    slurm_instance_manager_cls = SlurmSnapInstanceManager

    def __init__(self, *args):
        super().__init__(*args)

        # provides host port to slurmctld
        self.munge = MungeProvides(self, "munge")
```



Requires

```python

class SlurmCharm(CharmBase):
    _state = StoredState()
    slurm_instance_manager_cls = SlurmSnapInstanceManager

    def __init__(self, *args):
        super().__init__(*args)

        # provides host port to slurmctld
	self.munge = MungeRequires(self, "munge")

        self.framework.observe(
		self.munge.on.munge_available, self._on_munge_available
	)
	def _on_munge_available(self, event):
	    #write munge key to slurm snap
	    pass

```
