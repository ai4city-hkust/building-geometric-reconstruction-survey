# Section-by-Section Reading Guide

[Home](../README.md) · [Paper library](../PAPERS.md) · [Datasets & evaluation](datasets-and-evaluation.md)

This guide follows the manuscript's seven sections and summarizes every numbered technical subsection. Page references refer to the supplied 70-page PDF. Study names link directly to official paper sources; the complete bibliography is organized in the paper library.

<a id="s1"></a>
## 1. Introduction

*PDF pages 3-7.*

The survey places geometric structure at the center of building reconstruction. Its scope extends from closed footprint polygons through roof topology to full 3D wireframes and polyhedral models. This organization makes it possible to compare methods according to their outputs and constraints, rather than treating all building extraction as pixel classification.

The section relates reconstruction methods to sensor characteristics. Optical images provide rich appearance but require depth inference; stereo imagery recovers geometry through correspondence; LiDAR supplies direct coordinates but has gaps and uneven sampling. Fusion exploits these complementary strengths while introducing alignment requirements.

**Main conclusion:** model-driven fitting, data-driven learning, and hybrid reconstruction should be compared in the context of the available observations and the required geometric representation.

<a id="s2"></a>
## 2. 2D Building Outline Reconstruction

*PDF pages 7-18.*

The target is an instance-level vector outline with appropriate corners, boundary precision, and polygon topology.

### 2.1. From Optical Imagery

Optical reconstruction has evolved from segmenting building regions and vectorizing them afterward toward learning explicit polygon structure. The important distinction is where geometry enters the pipeline: in post-processing, in auxiliary supervision, or directly in the output representation.

#### 2.1.1. Segmentation-based Methods

Segmentation networks provide dense regional evidence, but their masks can round corners and introduce irregular edges. [Frame Field Learning](https://ieeexplore.ieee.org/document/9577910/) predicts contour directions to guide polygonization and preserve sharper structures. Related cadastral-boundary work applies these ideas to visible boundaries. The main limitation is error propagation from the mask into the final polygon.

#### 2.1.2. End-to-End Vector Polygon Generation

| Family | Summary | Key limitation |
| :--- | :--- | :--- |
| Sequential | [PolyMapper](https://ieeexplore.ieee.org/document/9008272/), [ConvGRU-based delineation](https://linkinghub.elsevier.com/retrieve/pii/S0924271621000551), and [VectorLLM](https://linkinghub.elsevier.com/retrieve/pii/S0924271626000250) generate ordered corners | Local errors can accumulate along long sequences |
| Graph and matching | [PolyWorld](https://ieeexplore.ieee.org/document/9880425/), [Re:PolyWorld](https://ieeexplore.ieee.org/document/10377491/), and [ABCNet](https://linkinghub.elsevier.com/retrieve/pii/S1569843225007186) infer connections between detected vertices | Missing or ambiguous corners undermine connectivity |
| RoI and query | [PolyR-CNN](https://linkinghub.elsevier.com/retrieve/pii/S0924271624003824), [RoIPoly](https://linkinghub.elsevier.com/retrieve/pii/S0924271625001364), [PolyBuilding](https://linkinghub.elsevier.com/retrieve/pii/S0924271623000813), and [PolyBuild](https://ieeexplore.ieee.org/document/10988661/) couple instance features with polygon prediction | Feature resolution and vertex capacity can limit fine detail |
| Hybrid and hierarchical | [HiSup](https://linkinghub.elsevier.com/retrieve/pii/S0924271623000667), [BD-Tracing](https://ieeexplore.ieee.org/document/10285447/), and [GCP](https://ieeexplore.ieee.org/document/11172367/) combine geometric supervision, tracing, or explicit simplification | Regularization can suppress valid small structures |

#### 2.1.3. Method Comparison and Analysis

Dense prediction retains strong regional evidence, sequences encode ordering naturally, graphs model connectivity explicitly, and query architectures enable parallel prediction. The survey emphasizes that architecture, training, and evaluation differ across studies. Their reported scores therefore do not establish a controlled ranking.

### 2.2. From LiDAR Point Clouds

For footprint extraction, 3D building points are often projected onto a horizontal plane. Direct spatial measurements reduce dependence on illumination, but uneven density, noise, and missing boundary points create a different regularization problem.

#### 2.2.1. Boundary Tracing and Regularization

Early methods impose local architectural constraints, as in [RMBR](https://linkinghub.elsevier.com/retrieve/pii/S0924271613002256), or balance fit and simplicity, as in [GMDL](https://www.isprs.org/proceedings/XXXVII/congress/3_pdf/11.pdf). Later methods coordinate the boundary globally: [Du et al.](https://ieeexplore.ieee.org/document/8681075/) combine contour decomposition with global regularization; [ATAS](https://linkinghub.elsevier.com/retrieve/pii/S0926580524000578) adapts tracing and optimizes neighboring segments; [Wu et al.](https://linkinghub.elsevier.com/retrieve/pii/S026322412503369X) use density-based corner selection to tolerate data gaps.

#### 2.2.2. Feature Fusion and Classification

[Du et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271616306438) combine point-level geometric features and grid-level information to improve building classification before regularization. Better separation of buildings from vegetation produces cleaner inputs, but classification alone does not produce a finished polygon.

#### 2.2.3. Method Comparison and Analysis

Strong geometric priors stabilize incomplete boundaries when the building satisfies those assumptions. Flexible tracing preserves irregular details but is more sensitive to the point distribution. Shape complexity, point density, and the pattern of missing observations must be considered together.

### 2.3. Summary

Optical methods must infer boundaries from appearance; LiDAR methods must organize sparse spatial samples into continuous geometry. Both need to preserve genuine detail while limiting noise, redundant vertices, and topological inconsistencies.

<a id="s3"></a>
## 3. 2.5D Building Roof Reconstruction

*PDF pages 18-29.*

The focus expands from the outer boundary to roof facets, junctions, ridges, and elevation. Full facade detail is outside the core 2.5D representation.

### 3.1. From Optical Imagery

Two complementary routes dominate: parsing a roof's structural graph, and directly estimating roof geometry or height. A planar graph is valuable structural information, but it is not automatically a metric 3D roof.

#### 3.1.1. Geometric Primitive Parsing

[Nauata and Furukawa](https://link.springer.com/chapter/10.1007/978-3-030-58598-3_42) combine primitive detection with relationship constraints. [PPGNet-based roof vectorization](https://isprs-archives.copernicus.org/articles/XLVI-4-W4-2021/85/2021/), [HEAT](https://ieeexplore.ieee.org/document/9878511/), [Conv-MPN](https://ieeexplore.ieee.org/document/9156819/), [RSGNN](https://linkinghub.elsevier.com/retrieve/pii/S092427162200065X), and [Roof-Former](https://ieeexplore.ieee.org/document/10282198/) learn junctions, edges, and their relationships using graph or attention mechanisms. [HAWP](https://ieeexplore.ieee.org/document/10243120/) contributes a general line representation; [directional primitive reconstruction](https://linkinghub.elsevier.com/retrieve/pii/S0924271626001735) combines complementary structural elements. [Kenzhebay](https://essay.utwente.nl/essays/91396) studies a segmentation-and-vectorization route using imagery and surface-height information.

The shared challenge is recovering complete connectivity when local primitives are weak, occluded, or missing.

#### 3.1.2. Direct 3D Plane and Height Inference

[PlaneRCNN](https://ieeexplore.ieee.org/document/8953257/) provides a general example of estimating planar geometry from an image, while [boundary-aware overhead reconstruction](https://ieeexplore.ieee.org/document/9156304/) combines outlines with predicted height. [Roof3D](https://isprs-annals.copernicus.org/articles/X-1-W1-2023/971/2023/) supports roof-plane and building-section learning. [KIBS](https://linkinghub.elsevier.com/retrieve/pii/S0924271624004210) infers 3D roof information through keypoints and height estimates. These routes move beyond graph connectivity but inherit ambiguity from monocular observations or dependence on auxiliary DSM quality.

#### 3.1.3. Method Comparison and Analysis

Primitive parsing offers explicit topology but depends on reliable detections. Direct inference supplies plane or height estimates but must resolve depth uncertainty. These approaches solve complementary parts of roof reconstruction and should be evaluated according to the geometry they actually produce.

### 3.2. From LiDAR Point Clouds

LiDAR makes roof elevations observable. The remaining challenge is converting unstructured samples into regular, connected roof surfaces.

#### 3.2.1. Model-Driven Approaches

Top-down methods fit parametric roof models or enforce architectural regularities. [RMBR](https://linkinghub.elsevier.com/retrieve/pii/S0924271613002256) illustrates rectangular decomposition; [Zhou and Neumann](https://ieeexplore.ieee.org/document/6247692/) discover relationships among locally fitted planes. Strong priors work well when they match the roof, but a restricted shape library cannot represent all architecture.

#### 3.2.2. Data-Driven Approaches

Bottom-up reconstruction extracts structure from the observations. Examples include [hierarchical plane clustering](https://www.mdpi.com/1424-8220/8/11/7323), [multiscale grids](https://ieeexplore.ieee.org/document/6779638/), [spatial-database workflows](https://www.tandfonline.com/doi/full/10.1080/13658816.2017.1301456), [roof topology cycles](https://linkinghub.elsevier.com/retrieve/pii/S0924271614001129), and [half-space modeling](https://www.mdpi.com/2072-4292/13/21/4430). [Point2Roof](https://linkinghub.elsevier.com/retrieve/pii/S0924271622002362) learns vertices and edges, while [RR-Net](https://ieeexplore.ieee.org/document/11218167/) emphasizes edge segmentation and wireframe recovery.

Here, "data-driven" includes bottom-up geometric algorithms as well as neural methods. It is not a synonym for deep learning.

#### 3.2.3. Method Comparison and Analysis

The distinction between top-down and bottom-up methods is largely about the form and strength of their priors. Flexible extraction can accommodate complex roofs, while constrained fitting is stable for regular ones. Learned edges may still require fitting and reconnection to obtain complete surfaces.

### 3.3. Summary

Successful roof reconstruction combines metric elevation with coherent topology. Optical methods rely on depth cues or auxiliary heights; LiDAR methods rely on coverage and geometric organization. In both cases, roof complexity exposes the trade-off between flexibility and regularity.

<a id="s4"></a>
## 4. 3D Building Model and Wireframe Reconstruction

*PDF pages 29-43.*

This section considers full building structure, including vertical surfaces and the relationships among vertices, edges, and faces. Wireframes, implicit fields, and closed meshes are different outputs with different validity requirements.

### 4.1. From Optical Imagery and Photogrammetric Point Clouds

Image-based methods either first recover dense geometry from multiple views or infer structural abstractions using stronger priors. Photogrammetric point clouds retain the uncertainty of the image-matching process that produced them.

#### 4.1.1. Multi-View Stereo-based Reconstruction

Multi-view correspondence produces depths, points, or meshes that require further abstraction. [Verdie et al.](https://dl.acm.org/doi/10.1145/2732527) regularize scene geometry; [Partovi et al.](https://www.mdpi.com/2072-4292/11/14/1660) fit roof hypotheses from satellite-derived evidence; [Li and Wu](https://www.mdpi.com/2072-4292/13/1/129) encode relations between building parts. [SAT2LOD2](https://isprs-archives.copernicus.org/articles/XLIII-B2-2022/379/2022/) and [PLANES4LOD2](https://linkinghub.elsevier.com/retrieve/pii/S0924271624001758) combine orthophotos and DSMs with plane or roof modeling. Occlusion, weak texture, and DSM errors remain important limitations.

#### 4.1.2. Single-Image Structural Inference and Generative Directions

[Alidoost et al.](https://www.mdpi.com/2072-4292/11/19/2219) infer height and roof structure from a single aerial image, while [Zhou et al.](https://ieeexplore.ieee.org/document/9010693/) use structural assumptions to recover 3D Manhattan wireframes. [DG-BRF](https://linkinghub.elsevier.com/retrieve/pii/S0924271625004563) introduces diffusion-guided geometric reasoning, and [Sat2City](https://ieeexplore.ieee.org/document/11446050/) studies city-scale generation. The survey distinguishes plausible urban generation from observation-faithful reconstruction of an individual building.

#### 4.1.3. Method Comparison and Analysis

Multiple views provide stronger direct geometric evidence, but their errors propagate into abstraction. Single-image methods reduce acquisition requirements while increasing dependence on priors. Generative outputs require checks of their correspondence with the actual scene.

### 4.2. From LiDAR Point Clouds

The problem becomes reconstructing structure from measured but incomplete and unevenly sampled geometry. The main families are explicit primitive assembly and learned structural prediction.

#### 4.2.1. Primitive Assembly and Optimization

[PolyFit](https://ieeexplore.ieee.org/document/8237520/) assembles candidate faces under geometric constraints. [City3D](https://www.mdpi.com/2072-4292/14/9/2254) addresses city-scale reconstruction and missing facade observations; [SimpliCity](https://ieeexplore.ieee.org/document/10678009/) emphasizes compact regularized models. [Manhattan-world reconstruction](https://link.springer.com/chapter/10.1007/978-3-319-46493-0_4) uses stronger orthogonal assumptions. [Loops2Roofs](https://dl.acm.org/doi/10.1145/3807955) introduces a generative loop representation at the boundary between explicit structure and learned generation.

The survey also lists [KIPPI](https://ieeexplore.ieee.org/document/8578430/); its cited publication concerns image partitioning. This guide does not attribute unverified 3D surface guarantees to that citation.

#### 4.2.2. Direct End-to-End Reconstruction

| Representation | Examples | Key idea |
| :--- | :--- | :--- |
| Vertices and edges | [Point2Roof](https://linkinghub.elsevier.com/retrieve/pii/S0924271622002362), [PBWR](https://ieeexplore.ieee.org/document/10656530/) | Learn geometric primitives and their connections |
| Autoregressive meshes | [Point2Building](https://linkinghub.elsevier.com/retrieve/pii/S092427162400279X) | Generate variable-size vertex and face sequences |
| Diffusion-assisted structure | [EdgeDiff](https://ieeexplore.ieee.org/document/11094351/), [BuildAnyPoint](https://openaccess.thecvf.com/content/CVPR2026/html/Hua_BuildAnyPoint_3D_Building_Structured_Abstraction_from_Diverse_Point_Clouds_CVPR_2026_paper.html) | Refine edges or recover intermediate geometric evidence |
| Implicit representations | [Chen et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271622002611) | Combine learned occupancy with surface extraction |
| Architectural programs | [ArcPro](https://ieeexplore.ieee.org/document/11092796/) | Predict a compact procedural description of structure |
| Supporting learning tasks | [City-BIS](https://linkinghub.elsevier.com/retrieve/pii/S1569843226000026), [self-supervised roof learning](https://ieeexplore.ieee.org/document/10423095/) | Improve instances or reduce annotation dependence |

#### 4.2.3. Method Comparison and Analysis

Explicit constraints are effective when the relevant surfaces are observed. Learned shape priors provide flexibility under sparse observations, but predicted wireframes are not necessarily closed surfaces, and generated mesh detail is not necessarily measured detail. Geometric fit, completeness, and compactness need separate assessment.

### 4.3. From Fused Image and Point Cloud Data

[Cheng et al. (2011)](https://doi.org/10.14358/pers.77.2.125) and [Cheng et al. (2013)](https://linkinghub.elsevier.com/retrieve/pii/S0143816612002990) combine image boundary evidence with LiDAR planes to refine 3D structure. [Awrangjeb et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271613001342) use imagery to support roof-plane extraction and reject vegetation. [Wang et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271617303593) investigate facade features with structural constraints.

#### 4.3.1. Method Comparison and Analysis

Fusion can improve boundary placement, surface interpretation, and facade detail. These benefits depend on calibration, registration, and consistency between observations. Misaligned or temporally mismatched modalities can instead introduce structural errors.

### 4.4. Summary

Different inputs and representations lead to different reconstruction uncertainties. Reliable 3D building models require the right balance of observational support, structural priors, explicit validation, and computational cost.

<a id="s5"></a>
## 5. Datasets and Evaluation

*PDF pages 43-49.*

### 5.1. Public Benchmark Datasets

The section maps datasets to the geometry they supervise: footprints, roof graphs, heights, wireframes, and meshes. It also includes datasets for supporting tasks such as multimodal semantic understanding and building instance segmentation. Geographic and architectural diversity matter when moving beyond a single benchmark.

### 5.2. Evaluation Metrics and Protocols

The survey recommends evaluating more than region overlap. Boundary position, corner angles, vertex complexity, edge connectivity, height error, and structural relationships capture different aspects of geometric quality. A fair comparison requires compatible datasets, input modalities, splits, tolerances, and output representations.

See the [dataset and metric guide](datasets-and-evaluation.md) for the complete named resource list and a task-oriented metric map.

<a id="s6"></a>
## 6. Discussion and Future Outlook

*PDF pages 48-54.*

### 6.1. Summary of Current State and Open Challenges

Four operational problems recur: irregular or invalid boundaries, incomplete 3D observations, expensive structural annotations, and difficult city-scale workflows. Geographic data and self-supervision can reduce annotation costs. Agent-assisted processing may coordinate tools, but the survey calls for intermediate validation, provenance, and human oversight where results are uncertain.

### 6.2. The Rise of Foundation Models

Diffusion methods offer structural completion, while vision-language models and language models provide semantic priors and sequential geometric prediction. Neural scene representations such as NeRF and 3D Gaussian Splatting offer additional routes toward scene reconstruction. These capabilities do not automatically produce accurate coordinates or valid explicit building geometry. Promising directions include geometric constraints, topology validation, and uncertainty estimation.

### 6.3. Deeper Data Fusion and Semantic Enrichment

Future models may combine imagery, LiDAR, SAR, thermal observations, and GIS information. The objective expands from geometric shape to semantically meaningful urban objects. Cross-modal alignment, differing resolutions, acquisition dates, and data quality must be handled explicitly. Semantic enrichment and interoperable representations support downstream analysis and simulation.

### 6.4. Scalability, Real-time Processing, and Dynamic Monitoring

Urban models need repeated updates as buildings are constructed or changed. Efficient processing, time-series observations, and change-aware reconstruction can support this transition. Dynamic digital twins require reliable temporal correspondence and update validation in addition to fast inference.

<a id="s7"></a>
## 7. Conclusion

*PDF pages 54-55.*

The survey traces a progression from manual digitization and raster extraction to direct geometric prediction. It identifies complementary roles for optical imagery, LiDAR, fusion, explicit regularization, and learned priors across 2D, 2.5D, and 3D reconstruction.

Architectural diversity, imperfect observations, and urban-scale computation remain unresolved challenges. The practical research goal is increasingly automated reconstruction that preserves metric fidelity, valid topology, interpretable structure, and usability for digital twins.
