st_gcn 

```
input: 
x: torch.Size([n, 3, 300, 25])
A: torch.Size([3, 25, 25])	

x, A = self.gcn(x, A)
	
output:
x: torch.Size([n, 64, 300, 25])  
A: torch.Size([3, 25, 25])
```



poseformer

```
in:
torch.Size([n, 3, 290, 25])

x = self.Spatial_forward_features(x)

out:
torch.Size([n, 290, 800])

```



x_scale

```
x_gcn: torch.Size([n, 64, 300, 25])
x_transformer: torch.Size([n, 64, 300, 25])

x_scale = torch.cat((x_transformer, x_gcn),1)
x_scale torch.Size([20, 128, 300, 25])

x_scale = x_gcn + x_transformer 
# torch.Size([2n, 64, 300, 25])
```

