**GCP Disk Resize**

If you need to resize a running GCP VM's disk space, go to "Disks" in the GCP sidebar...


<kbd>![GCP Compute Engine dashboard](https://github.com/Luct0r/assets/blob/master/GCP-Disks.png)</kbd>

Find and click on the VM, click "Edit", then add whatever is appropriate. Followed by the below commands once it is finished provisioning:

```
sudo apt install -y cloud-guest-utils
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1
```

Reference: [GCP Disk Resize](https://medium.com/google-cloud/resize-your-persist-disk-on-google-cloud-on-the-fly-b3491277b718)
