# nCRP
This is a repository and tutorial for the nested Chinese Restaurant process (https://github.com/Ferrumofomega/nCRP.git).

This model is implemented using Edward (http://edwardlib.org/).

This nCRP was used to model decision making using structured uncertainty in an OUP volumne on Transformational Experience.

 
## Non-Parametric Clustering Using the Nested Chinese Restaurant Process
 
The generative model we described for creating new food instances is the *nested Chinese Restaurant Process* (nCRP). 
The nCRP is an unsupervised, non-parametric, generative model for assigning probability distributions to 
branching tree structures. See Blei above for a more in-depth discussion of the nested Chinese Restaurant Process. 

While the model in the paper leverages the hierarchical categorization that the *nCRP* offers, our models offers a finite, deterministic tree depth. 
The original paper places an IID over the tree depth as well, enabling for an infinite depth to the trees.

## Model Definition

First we need to define a food object's partition, or it's possible paths throughout the structured generative model defined above. 

Here, consider a set of an **N** *i.i.d.* input food vectors, indicating an agent's previously eaten foods. 
Our model uses a three-level category hierarchy. The food vectors are partitioned into C level-one categories. 
We represent the partition via a vector v<sup>b</sup> of length **N**, where each v<sup>b<sub>n</sub></sup> in {1,....,C}. 

The **C** basic-level categories are then partitioned into **B** second-level categories (where **K**  <= **N**) 
which are represented via the vector v<sup>s<sub>n</sub></sup> of length **C**. 

Finally, the **B** second-level categories are then partitioned into **A** third-level categories which are represented 
via the vector v<sup>t<sub>n</sub></sup>. 
We define p<sub>n</sub> as the triple {v<sup>b<sub>n</sub></sup>, v<sup>s<sub>n</sub></sup>, v<sup>t<sub>n</sub></sup>}, which defines for each *n* in **N** a path through the three-level tree.
 
As the name suggests, the *nCRP* is composted of nested Chinese Restaurant Processes. The *CRP* provides a way to partition food instances at each level of the hierarchy as they enter which is represented via a single $\alpha parameter. 
Imagine a Chinese Restaurant with an infinite number of tables that can each seat an infinite number of persons. 
At a given time *t*, after a number of other people have been seated, the *CRP* provides the probability a person has of sitting at all the occupied tables, *and a new table*.  The *CRP* is defined as:
    
![Image](../rsc/img/nCRP_equation.gif?raw=true)
    
Where p<sup>i</sup> is the partition define above, $\alpha$<sub>CRP</sub> is the concentration parameter that encodes how frequently a new partition is produced, *K* is the total number of tables, tau<sub>i</sub> is the partition that food vector *n* is places at, and $\delta_{\tau}$ is the distribution that puts it's mass at a given partition, 
We embed a *CRP* *at each* category-level **A,B,C**. 
    
In our model we found that (2 .5 .5) for the $\alpha$ parameters in the *nCRP* corresponding to 'category', 'sub-category' and 'instance' level concentration parameters performed well.

This enables our agent to infer the placement of a novel experience with respect to an agent's previous structured knowledge and experiences, further informing their expected utility at a given time.
    
**Placement of new item in hierarchy** We considered first the location of the new food in the existing hierarchy. The agent places a greater degree of belief on the new food being a type of grape. 
  
[INSERT FIGURE]
