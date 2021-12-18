There are two types of #supervised #learning:

1) With #regression
2) With #classification 

This is an explanation of the concept of #regression:

![[DATA2/Week 7/Linear Regression.pdf#page=13]]

To have a #classification #algorithm instead, we'll have to use the logistical regression that uses this formula:
$$
g(z)=1 /\left(1+e^{-z}\right)
$$

This used instead of #linear #regression when the linear model gives us values that are outside the range $0 \leq x \leq 1$, because in #classification problems these are the only possible outcomes.

The above formula can be written in this way too:
$$
\frac{1}{1+e^{-\left(\emptyset_{0}+\emptyset_{1} x\right)}}
$$

Instead of getting the #slope and the #intersection values, we're going to get two $\emptyset$ parameters after our #logistical training (using a #dataset). Since the Y values represent a probability value, that's what we'll get if we try to predict using the #logistical #regression #formula.

We also have to check if these model are predicting values correctly: to do so, we'll be using a #confusion #matrix.

</br>

$$
\begin{array}{|l|c|c|c|}
\hline & \begin{array}{l}
\text { Predicted } \\
\text { Class (0) }
\end{array} & \begin{array}{l}
\text { Predicted } \\
\text { Class (1) }
\end{array} & \\
\hline \begin{array}{l}
\text { Actual } \\
\text { Class (0) }
\end{array} & \text { TN } & \text { FP } & \text { Total } \\
\hline \begin{array}{l}
\text { Actual } \\
\text { Class (1) }
\end{array} & \text { FN } & \text { TP } & \text { Total } \\
\hline & \text { Total } & \text { Total } & \\
\hline
\end{array}
$$
</br>

This #table, using some testing data to check the accuracy of the model, can add up how many times the model has done right or wrong and what it was supposed to predict.

</br>

$$
\begin{array}{|l|c|c|l|}
\hline \text { N=21 } & \begin{array}{c}
\text { Predicted } \\
\text { Class (0) }
\end{array} & \begin{array}{l}
\text { Predicted } \\
\text { Class (1) }
\end{array} & \\
\hline \text { Actual } & \text { TN } & \text { FP } & \text { Total= } \\
\text { Class (0) } & \text { [6] } & \text { [1] } & \text { [7] } \\
\hline \text { Actual } & \text { FN } & \text { TP } & \text { Total= } \\
\text { Class (1) } & \text { [4] } & \text { [10] } & \text { [14] } \\
\hline & \text { Total = } & \text { Total = } & \text { TOTAL= } \\
& \text { [10] } & \text { [11] } & \text { [21] } \\
\hline
\end{array}
$$

To find the #accuracy, we'll just add the number of times the #model predicted correctly and divide it by the number of guesses. The #error is just 1 minus the #accuracy.

There are other 3 types of measures that can be useful to know:

1) #Sensitivity: $\frac{TP}{TP+FN}$
2) #Specificity: $\frac{TN}{TN+FP}$
3) #PPV (Positive Predicted Value) or #Precision : $\frac{TP}{TP+FP}$

[[Lab 13 Supervised Learning and Logistic Regression|]]