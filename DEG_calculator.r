###   filter the gene which has low counts
library(edgeR)
library(tidyverse)
setwd('I:\\其他人\\葛敏\\rna-seq')
dir()
fpkmIsoOrd36 <- read.table("tpm_result.txt", sep = "\t", header = T)
order_frame <- c(1, 5, 6, 7, 11, 12, 13) # reorder the columns based on the requirement of your analyses
order_frame_noname <- order_frame[2:7]-1
fpkmIsoOrd36 <- fpkmIsoOrd36[order_frame]
dir()
x <- read.delim("counts_result.txt",header = TRUE, row.names = "Name")
x <- x[order_frame_noname]
counts <- read.table("counts_result.txt", sep = "\t", header = T)
counts <- counts[order_frame]
# group <- factor(c(1,1,1,1,1,1,1,1,
#                   2,2,2,2,2,2,2,2,
#                  3,3,3,3,3,
#                  4,4,4,4,4,
#                  5,5,5,5,5,
#                  6,6,6,6,6))

group <- factor(c(1,1,1,2,2,2))

y <- DGEList(counts=x,group=group)
y <- calcNormFactors(y)
design <- model.matrix(~group)
y <- estimateDisp(y,design)
fit <- glmQLFit(y,design)
qlf <- glmQLFTest(fit,coef=2)
topTags(qlf)


y$samples
# A requirement for expression in two or more libraries is used as the minimum number of samples in each group is three.
# This ensures that a gene will be retained if it is only expressed in both samples in group 3.
keep <- rowSums(cpm(y)>1) >= 3 
filY <- y[keep, , keep.lib.sizes=FALSE]
dim(filY$counts)
head(filY$counts)

###   filter the expressed gene
rowNam <- row.names(filY$counts)
rowNam <- as.data.frame(rowNam)
names(rowNam) <- "Name"
head(rowNam)
fpkmIsoOrdFil36 <- inner_join(fpkmIsoOrd36, rowNam, by = "Name")
countsIsoOrdFil36 <- inner_join(counts, rowNam, by = "Name")
dim(fpkmIsoOrdFil36)

write_tsv(countsIsoOrdFil36, "outCountsIsoOrdFil36.txt")
write_tsv(fpkmIsoOrdFil36, "outFpkmIsoOrdFil36.txt")

### DEG detection
library(edgeR)
dir()
df <- read.table("outCountsIsoOrdFil36.txt", sep = "\t", header = TRUE)
table.summary <- df
names(table.summary)
counts = table.summary[,c(2:7)] # 去掉不相关的列，仅保留需要计算P值的列
names(counts)
rownames(counts) = table.summary[,1]
grp = factor(rep(c("CK","Treatment"),times = c(3,3))) # 标记比较的分组以及每组有多少重复
summarized = DGEList(counts,lib.size = colSums(counts), group = grp)
disp = estimateCommonDisp(summarized)
tested = exactTest(disp)
options ( max.print = 999999)
sink("outFdr36Grp3.txt") #标记输出的文件名
topTags (tested, n = 999999)
sink()
