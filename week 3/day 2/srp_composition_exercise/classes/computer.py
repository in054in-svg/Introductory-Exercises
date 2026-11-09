class Computer:
    def __init__(self, cpu, ram, disk):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        
    def __str__(self):
        return f'{self.cpu.cores}-core {self.cpu.GHz_speed}Hz, {self.ram.gb}GB RAM, {self.disk.gb}GB SSD'
    
    def can_run(self, min_core: int, min_disk_gb: int):
        return min_core >= self.cpu.cores and min_disk_gb >= self.disk.gb