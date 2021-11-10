library(ggplot2)
library(reshape2)

input_name <- '2021.11_list.tsv'
base_name <- strsplit(input_name,split = ".tsv",fixed = T)
date_list <- read.csv(input_name,sep = '\t',check.names = F)

date_list[is.na(date_list)] <- 0 
dt <- data.frame(date_list[1],apply(date_list[,2:31],2,as.numeric))
df <- melt(date_list,id.vars=c('Things'))

png(paste0(base_name,'.png'),width = 1080,height = 480)
ggplot(df,aes(x=variable,y=Things))+
  geom_tile(alpha=0.7,aes(fill=value))+
  labs(x='Date',y="",title=base_name)+
  theme(panel.grid = element_blank(),
        plot.title = element_text(hjust = 0.5,size = 20,family = "serif"),
        axis.text.y = element_text(family ="serif",size = 14,color="black"))+
  scale_fill_gradient(low = "white", high = "darkblue")
dev.off()
