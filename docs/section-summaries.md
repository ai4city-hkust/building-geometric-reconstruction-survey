# Section-by-Section Reading Guide

[Home](../README.md) · [Paper library](../PAPERS.md) · [Datasets & evaluation](datasets-and-evaluation.md)

This guide follows the seven sections and every numbered technical subsection in the maintainer-supplied LaTeX manuscript. It summarizes the active text and comparison tables, excluding commented-out drafts. Study names link directly to official paper sources; the complete catalog is organized in the paper library. Ambiguities in the source are recorded separately in the [editorial notes](editorial-notes.md).

<a id="s1"></a>
## 1. Introduction

The survey places geometric structure at the center of building reconstruction. Its scope extends from closed footprint polygons through roof topology to full 3D wireframes and polyhedral models. This organization makes it possible to compare methods according to their outputs and constraints, rather than treating all building extraction as pixel classification.

The motivation spans urban planning, disaster management, energy and environmental assessment, smart cities, and digital twins. These applications require more than building presence: they need boundaries, heights, connected surfaces, and geometric representations suitable for analysis. The review addresses the transition from raster extraction to explicit geometry across output dimensions and sensing modalities.

The section relates reconstruction methods to sensor characteristics. Optical images provide rich appearance but require depth inference; stereo imagery recovers geometry through correspondence; LiDAR supplies direct coordinates but has gaps and uneven sampling. Fusion exploits these complementary strengths while introducing alignment requirements.

**Literature selection.** The manuscript reports searches in Web of Science, Scopus, IEEE Xplore, and Google Scholar, mainly spanning 2000-2026 and including relevant journal and conference work. Search terms cover building footprints, roofs, 3D reconstruction, wireframes, optical imagery, LiDAR, and point clouds. The core inclusion criterion is reconstruction of explicit 2D, 2.5D, or 3D building geometry; work limited to semantic classification or raster segmentation is outside that core scope. Reference-list snowballing supplements the search. Background surveys and supporting representations remain relevant context, rather than all being standalone reconstruction systems.

**Main conclusion:** model-driven fitting, bottom-up geometric or learned methods, and hybrid reconstruction should be compared in the context of the available observations and required output. Architectural diversity, occlusion, noise, and city-scale automation remain cross-cutting limitations.

<a id="s2"></a>
## 2. 2D Building Outline Reconstruction

The target is an instance-level vector outline with appropriate corners, boundary precision, and polygon topology.

### 2.1. From Optical Imagery

Optical reconstruction has evolved from segmenting building regions and vectorizing them afterward toward learning explicit polygon structure. The important distinction is where geometry enters the pipeline: in post-processing, in auxiliary supervision, or directly in the output representation.

#### 2.1.1. Segmentation-based Methods

Segmentation networks provide dense regional evidence, but their masks can round corners and introduce irregular edges. [Frame Field Learning](https://ieeexplore.ieee.org/document/9577910/) jointly learns masks and contour directions, then uses an Active Skeleton Model for polygonization, including shared-wall handling. [Tareke et al.](https://ieeexplore.ieee.org/document/10282644/) combine U-Net and frame-field learning with contour processing for visible cadastral boundaries. Neither approach makes the final geometry independent of segmentation and post-processing.

The cross-region study by [Buyukdemircioglu et al.](https://isprs-archives.copernicus.org/articles/XLVIII-1-W6-2025/47/2025/) reinforces the difference between pixel agreement and geometric boundary quality. Generalization and polygon validity need evaluation beyond an in-domain segmentation score.

#### 2.1.2. End-to-End Vector Polygon Generation

| Family | Summary | Key limitation |
| :--- | :--- | :--- |
| Sequential | [PolyMapper](https://ieeexplore.ieee.org/document/9008272/), [ConvGRU-based delineation](https://linkinghub.elsevier.com/retrieve/pii/S0924271621000551), and [VectorLLM](https://linkinghub.elsevier.com/retrieve/pii/S0924271626000250) generate ordered corners | Local errors can accumulate along long sequences |
| Graph and matching | [PolyWorld](https://ieeexplore.ieee.org/document/9880425/), [Re:PolyWorld](https://ieeexplore.ieee.org/document/10377491/), and [ABCNet](https://linkinghub.elsevier.com/retrieve/pii/S1569843225007186) infer connections between detected vertices | Missing or ambiguous corners undermine connectivity |
| RoI and query | [PolyR-CNN](https://linkinghub.elsevier.com/retrieve/pii/S0924271624003824), [RoIPoly](https://linkinghub.elsevier.com/retrieve/pii/S0924271625001364), [PolyBuilding](https://linkinghub.elsevier.com/retrieve/pii/S0924271623000813), and [PolyBuild](https://ieeexplore.ieee.org/document/10988661/) couple instance features with polygon prediction | Feature resolution and vertex capacity can limit fine detail |
| Hybrid and hierarchical | [HiSup](https://linkinghub.elsevier.com/retrieve/pii/S0924271623000667), [BD-Tracing](https://ieeexplore.ieee.org/document/10285447/), and [GCP](https://ieeexplore.ieee.org/document/11172367/) combine geometric supervision, tracing, or explicit simplification | Regularization can suppress valid small structures |

Sequential models differ in their use of context: PolyMapper uses recurrent decoding, the ConvGRU approach adds global context and boundary refinement, and VectorLLM treats corners as an autoregressive multimodal prediction task. Graph methods instead optimize vertex connections: PolyWorld uses attention and optimal transport, Re:PolyWorld adds edge-aware reasoning, and ABCNet uses bipartite matching and assignment.

Within the query family, PolyR-CNN couples vertex proposals with instance features, RoIPoly filters redundant vertex queries, PolyBuilding uses a fixed vertex budget with suppression, and PolyBuild refines an initial contour. The hybrid category is not interchangeable with direct polygon regression: HiSup supervises vertices, segments, and masks but still needs polygonization; BD-Tracing uses bidirectional nonrecurrent tracing; GCP combines contour prediction with dynamic-programming-based collinearity regularization.

#### 2.1.3. Method Comparison and Analysis

Dense prediction retains strong regional evidence, sequences encode ordering naturally, graphs model connectivity explicitly, and query architectures enable parallel prediction. The survey emphasizes that architecture, training, and evaluation differ across studies. Their reported scores therefore do not establish a controlled ranking.

### 2.2. From LiDAR Point Clouds

For footprint extraction, 3D building points are often projected onto a horizontal plane. Direct spatial measurements reduce dependence on illumination, but uneven density, noise, and missing boundary points create a different regularization problem.

#### 2.2.1. Boundary Tracing and Regularization

Early methods impose local architectural constraints, as in [RMBR](https://linkinghub.elsevier.com/retrieve/pii/S0924271613002256), or balance fit and simplicity, as in [GMDL](https://www.isprs.org/proceedings/XXXVII/congress/3_pdf/11.pdf). Later methods coordinate the boundary globally: [Du et al.](https://ieeexplore.ieee.org/document/8681075/) combine contour decomposition with global regularization; [ATAS](https://linkinghub.elsevier.com/retrieve/pii/S0926580524000578) adapts tracing and optimizes neighboring segments; [Wu et al.](https://linkinghub.elsevier.com/retrieve/pii/S026322412503369X) use density-based corner selection to tolerate data gaps.

The comparison table also includes [Nalini et al.](https://isprs-annals.copernicus.org/articles/X-5-W2-2025/429/2025/), combining plane detection and boundary tracing. Rectangular decomposition, direction quantization, and adaptive tracing impose different assumptions; their outputs should not all be described as unrestricted outline recovery.

#### 2.2.2. Feature Fusion and Classification

[Du et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271616306438) combine point-level normal-variation features with grid-level gray-level co-occurrence texture and graph-cut classification before boundary extraction. Better separation of buildings from vegetation produces cleaner inputs, but classification alone does not produce a finished polygon. Here, feature fusion occurs within LiDAR-derived representations, not between optical images and LiDAR sensors.

#### 2.2.3. Method Comparison and Analysis

Strong geometric priors stabilize incomplete boundaries when the building satisfies those assumptions. Flexible tracing preserves irregular details but is more sensitive to the point distribution. Shape complexity, point density, and the pattern of missing observations must be considered together.

### 2.3. Summary

Optical methods must infer boundaries from appearance; LiDAR methods must organize sparse spatial samples into continuous geometry. Both need to preserve genuine detail while limiting noise, redundant vertices, and topological inconsistencies.

<a id="s3"></a>
## 3. 2.5D Building Roof Reconstruction

The focus expands from the outer boundary to roof facets, junctions, ridges, and elevation. Full facade detail is outside the core 2.5D representation.

### 3.1. From Optical Imagery

Two complementary routes dominate: parsing a roof's structural graph, and directly estimating roof geometry or height. A planar graph is valuable structural information, but it is not automatically a metric 3D roof.

#### 3.1.1. Geometric Primitive Parsing

[Nauata and Furukawa](https://link.springer.com/chapter/10.1007/978-3-030-58598-3_42) combine primitive detection with relationship constraints. [PPGNet-based roof vectorization](https://isprs-archives.copernicus.org/articles/XLVI-4-W4-2021/85/2021/), [HEAT](https://ieeexplore.ieee.org/document/9878511/), [Conv-MPN](https://ieeexplore.ieee.org/document/9156819/), [RSGNN](https://linkinghub.elsevier.com/retrieve/pii/S092427162200065X), and [Roof-Former](https://ieeexplore.ieee.org/document/10282198/) learn junctions, edges, and their relationships using graph or attention mechanisms. [HAWP](https://ieeexplore.ieee.org/document/10243120/) contributes a general line representation; [directional primitive reconstruction](https://linkinghub.elsevier.com/retrieve/pii/S0924271626001735) combines complementary structural elements. [Kenzhebay](https://essay.utwente.nl/essays/91396) studies a segmentation-and-vectorization route using imagery and surface-height information.

The shared challenge is recovering complete connectivity when local primitives are weak, occluded, or missing.

The mechanisms are complementary: integer programming enforces primitive relationships; PPGNet predicts junction adjacency; HEAT reasons jointly about candidate edges with attention; Conv-MPN preserves spatial edge information during message passing; RSGNN combines Hough-based line priors and graph refinement; Roof-Former fuses multiscale features and segmentation cues. Yu et al. combine directional junctions and line primitives with matching and tracing. Kenzhebay uses RGB and normalized DSM evidence before skeletonization and vectorization. HAWP supplies general 2D line and junction cues, not roof heights on its own.

#### 3.1.2. Direct 3D Plane and Height Inference

[PlaneRCNN](https://ieeexplore.ieee.org/document/8953257/) provides a general example of estimating planar geometry from an image, while [boundary-aware overhead reconstruction](https://ieeexplore.ieee.org/document/9156304/) combines outlines with predicted height. [Roof3D](https://isprs-annals.copernicus.org/articles/X-1-W1-2023/971/2023/) supports roof-plane and building-section learning. [KIBS](https://linkinghub.elsevier.com/retrieve/pii/S0924271624004210) infers 3D roof information through keypoints and height estimates. These routes move beyond graph connectivity but inherit ambiguity from monocular observations or dependence on auxiliary DSM quality.

Their outputs differ materially. PlaneRCNN estimates masks and plane parameters and is a general planar-reconstruction reference with indoor evaluation. The boundary-aware approach predicts outlines and heights but does not resolve detailed roof slopes. Roof3D combines RGB and DSM inputs for roof-plane and section segmentation followed by polygonization. KIBS uses roof-section segmentation, discrete keypoint-height prediction, and Delaunay triangulation; quantized heights remain a limitation. These are not four equivalent single-image, complete-roof reconstruction systems.

#### 3.1.3. Method Comparison and Analysis

Primitive parsing offers explicit topology but depends on reliable detections. Direct inference supplies plane or height estimates but must resolve depth uncertainty. These approaches solve complementary parts of roof reconstruction and should be evaluated according to the geometry they actually produce.

### 3.2. From LiDAR Point Clouds

LiDAR makes roof elevations observable. The remaining challenge is converting unstructured samples into regular, connected roof surfaces.

#### 3.2.1. Model-Driven Approaches

Top-down methods fit parametric roof models or enforce architectural regularities. [RMBR](https://linkinghub.elsevier.com/retrieve/pii/S0924271613002256) illustrates rectangular decomposition; [Zhou and Neumann](https://ieeexplore.ieee.org/document/6247692/) discover relationships among locally fitted planes. Strong priors work well when they match the roof, but a restricted shape library cannot represent all architecture.

#### 3.2.2. Data-Driven Approaches

Bottom-up reconstruction extracts structure from the observations. Examples include [hierarchical plane clustering](https://www.mdpi.com/1424-8220/8/11/7323), [multiscale grids](https://ieeexplore.ieee.org/document/6779638/), [spatial-database workflows](https://www.tandfonline.com/doi/full/10.1080/13658816.2017.1301456), [roof topology cycles](https://linkinghub.elsevier.com/retrieve/pii/S0924271614001129), and [half-space modeling](https://www.mdpi.com/2072-4292/13/21/4430). [Point2Roof](https://linkinghub.elsevier.com/retrieve/pii/S0924271622002362) learns vertices and edges, while [RR-Net](https://ieeexplore.ieee.org/document/11218167/) emphasizes edge segmentation and wireframe recovery.

Here, "data-driven" includes bottom-up geometric algorithms as well as neural methods. It is not a synonym for deep learning.

The geometric pipelines have distinct intermediate representations. Dorninger and Pfeifer cluster plane parameters in a four-dimensional feature space. Chen et al. combine coarse normalized DSM evidence and fine-grid roof details. Cao et al. integrate building clustering, boundary regularization, planar patches, and patch intersections in a spatial-database workflow. Perera and Maas use closed cycles in roof topology graphs to recover corners, whereas Bizjak et al. combine half-spaces with **additional 2D outlines**, rather than LiDAR alone.

Point2Roof uses point features and paired attention to predict vertices and edges. RR-Net instead learns edge segmentation and denoising, then fits lines, reconnects corners, and reconstructs planes. Joint learning reduces some intermediate dependencies, but neither learned edges nor detected planes alone guarantee a complete roof surface.
#### 3.2.3. Method Comparison and Analysis

The distinction between top-down and bottom-up methods is largely about the form and strength of their priors. Flexible extraction can accommodate complex roofs, while constrained fitting is stable for regular ones. Learned edges may still require fitting and reconnection to obtain complete surfaces.

### 3.3. Summary

Successful roof reconstruction combines metric elevation with coherent topology. Optical methods rely on depth cues or auxiliary heights; LiDAR methods rely on coverage and geometric organization. In both cases, roof complexity exposes the trade-off between flexibility and regularity.

<a id="s4"></a>
## 4. 3D Building Model and Wireframe Reconstruction

This section considers full building structure, including vertical surfaces and the relationships among vertices, edges, and faces. Wireframes, implicit fields, and closed meshes are different outputs with different validity requirements.

### 4.1. From Optical Imagery and Photogrammetric Point Clouds

Image-based methods either first recover dense geometry from multiple views or infer structural abstractions using stronger priors. Photogrammetric point clouds retain the uncertainty of the image-matching process that produced them.

#### 4.1.1. Multi-View Stereo-based Reconstruction

Multi-view correspondence produces depths, points, or meshes that require further abstraction. [Verdie et al.](https://dl.acm.org/doi/10.1145/2732527) regularize scene geometry; [Partovi et al.](https://www.mdpi.com/2072-4292/11/14/1660) fit roof hypotheses from satellite-derived evidence; [Li and Wu](https://www.mdpi.com/2072-4292/13/1/129) encode relations between building parts. [SAT2LOD2](https://isprs-archives.copernicus.org/articles/XLIII-B2-2022/379/2022/) and [PLANES4LOD2](https://linkinghub.elsevier.com/retrieve/pii/S0924271624001758) combine orthophotos and DSMs with plane or roof modeling. Occlusion, weak texture, and DSM errors remain important limitations.

The manuscript contrasts correspondence engines such as PatchMatch and MVSNet with the subsequent structured-modeling stage. Verdie et al. use semantic classification and min-cut selection to abstract an MVS mesh. Partovi et al. combine stereo DSMs and optical imagery with footprint decomposition, roof-type classification, and parametric fitting. Li and Wu use relation-constrained constructive-solid-geometry / boundary-representation trees to produce CityGML-compatible solids. SAT2LOD2 uses roof extraction and rule-based fitting; PLANES4LOD2 introduces depth-attention segmentation of building parts and roof planes before geometric assembly. Better intermediate geometry does not remove the need for closure, topology, and abstraction checks.

#### 4.1.2. Single-Image Structural Inference and Generative Directions

[Alidoost et al.](https://www.mdpi.com/2072-4292/11/19/2219) predict normalized DSMs and roof lines from a single aerial image, then fit LoD models. [Zhou et al.](https://ieeexplore.ieee.org/document/9010693/) combine junctions, lines, depth, vanishing points, and occlusion reasoning to recover 3D Manhattan wireframes. Their orthogonal assumptions and domain-dependent height inference should not be generalized to arbitrary buildings.

[DG-BRF](https://linkinghub.elsevier.com/retrieve/pii/S0924271625004563) uses diffusion-guided roof/facade segmentation and geometric matching for off-nadir footprints and heights. [Sat2City](https://ieeexplore.ieee.org/document/11446050/) instead uses cascaded latent diffusion for city geometry and appearance. Its reported pipeline is **height-field-conditioned**, as specified in the survey's comparison table and the [original paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Hua_Sat2City_3D_City_Generation_from_A_Single_Satellite_Image_with_ICCV_2025_paper.pdf); it should not be read as a controlled demonstration of metric building recovery from unassisted RGB alone. Plausible city generation and observation-faithful wireframe reconstruction are different evaluation tasks.

The manuscript connects this generative direction to BuildAnyPoint, but the input modalities remain distinct: Sat2City conditions urban generation on a height-field representation, whereas BuildAnyPoint recovers a point representation before conditional mesh generation from point-cloud observations. This conceptual connection does not reclassify BuildAnyPoint as an image-only method.

#### 4.1.3. Method Comparison and Analysis

Multiple views provide stronger direct geometric evidence, but their errors propagate into abstraction. Single-image methods reduce acquisition requirements while increasing dependence on priors. Generative outputs require checks of their correspondence with the actual scene.

### 4.2. From LiDAR Point Clouds

The problem becomes reconstructing structure from measured but incomplete and unevenly sampled geometry. The main families are explicit primitive assembly and learned structural prediction.

#### 4.2.1. Primitive Assembly and Optimization

[Dorninger and Pfeifer](https://www.mdpi.com/1424-8220/8/11/7323) combine plane clustering, alpha-shape outlines, and regularization, with manual completion still noted in the comparison table. [PolyFit](https://ieeexplore.ieee.org/document/8237520/) intersects detected planes into candidate faces and selects a compact watertight surface through binary optimization. It requires the necessary supporting planes to be detected.

[City3D](https://www.mdpi.com/2072-4292/14/9/2254) infers missing vertical walls from height-map and boundary evidence and extends face selection with building-specific constraints. [SimpliCity](https://ieeexplore.ieee.org/document/10678009/) regularizes a 2D partition before 3D extrusion, using airborne points and footprints to preserve planar roofs and vertical discontinuities. [Manhattan-world reconstruction](https://link.springer.com/chapter/10.1007/978-3-319-46493-0_4) fits axis-aligned boxes and selects them with an MRF, restricting the supported architecture.

The survey also lists [KIPPI](https://ieeexplore.ieee.org/document/8578430/); its cited publication concerns image partitioning. This guide does not attribute unverified 3D surface guarantees to that citation.

#### 4.2.2. Direct End-to-End Reconstruction

| Representation | Examples | Key idea |
| :--- | :--- | :--- |
| Vertices and edges | [Point2Roof](https://linkinghub.elsevier.com/retrieve/pii/S0924271622002362), [PBWR](https://ieeexplore.ieee.org/document/10656530/) | Learn geometric primitives and their connections |
| Autoregressive meshes | [Point2Building](https://linkinghub.elsevier.com/retrieve/pii/S092427162400279X) | Generate variable-size vertex and face sequences |
| Diffusion-assisted structure | [EdgeDiff](https://ieeexplore.ieee.org/document/11094351/), [BuildAnyPoint](https://openaccess.thecvf.com/content/CVPR2026/html/Hua_BuildAnyPoint_3D_Building_Structured_Abstraction_from_Diverse_Point_Clouds_CVPR_2026_paper.html) | Refine edges or recover intermediate geometric evidence |
| Implicit representations | [Chen et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271622002611) | Combine learned occupancy with surface extraction |
| Architectural programs | [ArcPro](https://ieeexplore.ieee.org/document/11092796/) | Predict a compact procedural description of structure |
| Generative roof loops | [Loops2Roofs](https://dl.acm.org/doi/10.1145/3807955) | Generate polygonal roof loops with diffusion and neural stitching |
| Supporting learning tasks | [City-BIS](https://linkinghub.elsevier.com/retrieve/pii/S1569843226000026), [self-supervised roof learning](https://ieeexplore.ieee.org/document/10423095/) | Improve instances or reduce annotation dependence |

**Explicit predictions.** Point2Roof predicts roof vertices and edges; PBWR directly regresses parameterized edges with Transformer features and edge nonmaximum suppression. Their wireframe outputs do not by themselves establish a closed mesh or full facade reconstruction.

**Generative predictions.** Point2Building autoregressively emits vertices and faces. EdgeDiff generates edges by conditional denoising. BuildAnyPoint uses Loca-DiT to recover denser, more uniform points, followed by a decoder-only Transformer for mesh generation; its inputs include LiDAR, photogrammetric, and other sparse point sets. ArcPro generates a domain-specific architectural program whose primitives produce a compact mesh. These approaches differ in representation, topology constraints, and computational cost.

**Alternative and supporting tasks.** Chen et al. combine learned occupancy with MRF-based surface extraction. City-BIS segments building instances before reconstruction; it is not itself a mesh generator. Yang et al. use self-supervised pretraining and partial labeled fine-tuning for roof wireframes, not label-free full-building modeling. Loops2Roofs is included here as a generative roof-mesh direction, following the manuscript's comparison table, rather than as deterministic primitive assembly or a demonstrated raw-LiDAR reconstruction pipeline.

#### 4.2.3. Method Comparison and Analysis

Explicit constraints are effective when the relevant surfaces are observed. Learned shape priors provide flexibility under sparse observations, but predicted wireframes are not necessarily closed surfaces, and generated mesh detail is not necessarily measured detail. Geometric fit, completeness, and compactness need separate assessment.

### 4.3. From Fused Image and Point Cloud Data

[Cheng et al. (2011)](https://doi.org/10.14358/pers.77.2.125) and [Cheng et al. (2013)](https://linkinghub.elsevier.com/retrieve/pii/S0143816612002990) combine image boundary evidence with LiDAR planes to refine 3D structure. [Awrangjeb et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271613001342) use imagery to support roof-plane extraction and reject vegetation. [Wang et al.](https://linkinghub.elsevier.com/retrieve/pii/S0924271617303593) investigate facade features with structural constraints.

The integration happens at different stages. The 2011 boundary method projects LiDAR into calibrated images and intersects camera rays with LiDAR-derived planes. The 2013 method combines segmented roof points with multi-view line information to preserve roof steps. Multispectral guidance improves roof-plane selection in the vegetation-rejection method. For facades, EDLines and statistical line validation provide image features that are mapped into 3D and refined with RANSAC. These outputs are boundaries, roof lines, planes, or facade features, not four interchangeable complete-building mesh systems.

#### 4.3.1. Method Comparison and Analysis

Fusion can improve boundary placement, surface interpretation, and facade detail. These benefits depend on calibration, registration, and consistency between observations. Misaligned or temporally mismatched modalities can instead introduce structural errors.

### 4.4. Summary

Different inputs and representations lead to different reconstruction uncertainties. Reliable 3D building models require the right balance of observational support, structural priors, explicit validation, and computational cost.

<a id="s5"></a>
## 5. Datasets and Evaluation

### 5.1. Public Benchmark Datasets

The section maps datasets to the geometry they supervise: footprints, roof graphs, heights, wireframes, and meshes. It also includes datasets for supporting tasks such as multimodal semantic understanding and building instance segmentation. Geographic and architectural diversity matter when moving beyond a single benchmark.

| Resource family | Coverage in the manuscript | Important distinction |
| :--- | :--- | :--- |
| Footprints and polygon maps | CrowdAI, WHU, Inria, SpaceNet, Deventer-512 | Masks, building polygons, and all-class vector maps are not identical annotation targets |
| Roof topology and height | VWB, Enschede, Boston / BONAI; Roof3D in Section 3 | Image-plane roof graphs alone do not supply metric elevations; Roof3D adds RGB/DSM plane and section evidence |
| Structured 3D buildings | BuildingWF, BuildingWorld, and Building3D | BuildingWF supplies synthetic multi-view observations and 3D wireframes; geographic diversity and roof/full-building coverage vary across resources |
| Supporting scene understanding | Map2ImLas, City-BIS, Structured3D | Aligned semantic labels, building instances, and synthetic scene structure support different pipeline stages |

BuildingWorld broadens architectural and geographic coverage with LoD2 models and real/simulated airborne LiDAR. Building3D supplies urban roof points, meshes, and wireframes for supervised and self-supervised learning. Map2ImLas aligns 2D and 3D semantics; City-BIS provides instance separation; Structured3D provides synthetic primitive-and-relationship annotations. None should be assumed to share the same reconstruction ground truth.

The manuscript places BuildingWF in its 2.5D discussion, but the [cited source](https://arxiv.org/abs/2208.11948) defines synthetic multi-view images with ground-truth **3D building wireframes**, used to learn reconstruction from 3D line clouds. The dataset map therefore states its actual annotations rather than reducing it to a 2D roof-graph benchmark.

### 5.2. Evaluation Metrics and Protocols

The survey recommends evaluating more than region overlap. Boundary position, corner angles, vertex complexity, edge connectivity, height error, and structural relationships capture different aspects of geometric quality. A fair comparison requires compatible datasets, input modalities, splits, tolerances, and output representations.

Region and instance measures include FCSP, AFI, and AP/AR. Polygon quality adds PoLiS, boundary AP, maximum tangent-angle error, vertex redundancy, and complexity-aware IoU. NFA assesses statistical support for line features. Wireframes require matched corner/edge precision and recall, F1, and structural overlap such as sIoU. Height and surface assessment uses RMSE, height-threshold coverage such as `e_0.5`, and task-specific distances. Extended Attribute Adjacency Graphs (EAAG) describe structural relationships for model abstraction; the graph notation alone is not a scalar accuracy score.

The source's comparison tables mix datasets, units, output types, and matching rules. Their numerical results are study-specific evidence, not a common leaderboard. The guide therefore retains method mechanisms and limitations without implying that a higher number from another experimental setting proves superiority.

See the [dataset and metric guide](datasets-and-evaluation.md) for the complete named resource list and a task-oriented metric map.

<a id="s6"></a>
## 6. Discussion and Future Outlook

### 6.1. Summary of Current State and Open Challenges

Four operational problems recur:

- **Boundary and topology failures:** varying scales and roof layouts, confusion with visually similar nonbuildings, vegetation, shadows, and heterogeneous roof appearance can fragment polygons and invalidate meshes.
- **Incomplete 3D observations:** sparse or uneven sampling and missing facades stress both explicit fitting and learned prediction. Orthogonality and parallelism stabilize regular architecture but can suppress free-form or non-Manhattan geometry.
- **Annotation bottlenecks:** vector and 3D labels are expensive. OpenStreetMap, cadastral maps, and existing city models can supply pseudo-labels through coordinate matching, alignment, and projection; label reliability still needs checking.
- **Workflow integration:** agents can coordinate preprocessing, tool selection, reconstruction, and quality control. Incorrect tools, parameters, or intermediate interpretations can propagate errors, while stochastic decisions affect reproducibility. The manuscript calls for constrained tools, intermediate geometric validation, provenance, and human supervision of uncertain cases.

### 6.2. The Rise of Foundation Models

**Diffusion and generative priors.** EdgeDiff, DG-BRF, and BuildAnyPoint apply generative reasoning to different outputs: edges, roof/facade evidence, and an intermediate point representation followed by meshes. They can support completion under weak observations, but generated structure still needs metric and topological validation. Their inclusion in this outlook does not make every task-specific diffusion model a general-purpose foundation model.

**Neural scene representations.** NeRF and 3D Gaussian Splatting provide appearance-aware scene representations, with potential for surface reconstruction beyond novel-view rendering. [ULSR-GS](https://linkinghub.elsevier.com/retrieve/pii/S092427162500396X) uses scene partitioning, multi-view-guided densification, and depth/normal consistency for urban-scale aerial surface recovery. The unresolved step is converting these representations into explicit, connected building geometry; rendering quality is not a proxy for polygon or mesh validity.

**Vision-language and language models.** Semantic knowledge can extend recognition beyond narrowly defined visual classes. VectorLLM demonstrates sequential building-corner prediction, but coordinate errors can accumulate during autoregressive decoding, and semantic reasoning does not guarantee spatial precision. The manuscript identifies geometry-constrained generation, topology checks, uncertainty assessment, and computational efficiency as research needs rather than established zero-shot reconstruction capabilities.

### 6.3. Deeper Data Fusion and Semantic Enrichment

Future models may combine imagery, LiDAR, SAR, thermal observations, and GIS information. The objective expands from geometric shape to semantically meaningful urban objects. Cross-modal alignment, differing resolutions, acquisition dates, and data quality must be handled explicitly. Semantic enrichment and interoperable representations support downstream analysis and simulation.

The outlook spans multiscale semantic representations, from footprints to detailed building structure, and standards such as CityGML. This is a long-term interoperability objective; it does not mean that the surveyed airborne or overhead-image methods already recover interior geometry. Uncertainty in one modality should not be silently converted into a precise structural claim in the fused model.

### 6.4. Scalability, Real-time Processing, and Dynamic Monitoring

Urban models need repeated updates as buildings are constructed or changed. Efficient processing, time-series observations, and change-aware reconstruction can support this transition. Dynamic digital twins require reliable temporal correspondence and update validation in addition to fast inference.

The manuscript links lightweight computation and edge deployment to rapid disaster response. It discusses time-series optical, SAR, and night-light observations for construction monitoring and deformation analysis, with emergency-hospital construction and pre-collapse subsidence as application examples. These motivate updating geometry with temporal evidence, rather than treating each reconstruction as a permanent snapshot. Monitoring change or deformation is not itself a guarantee of reliable structural-failure prediction.

<a id="s7"></a>
## 7. Conclusion

The survey traces a progression from manual digitization and raster extraction to direct geometric prediction. It identifies complementary roles for optical imagery, LiDAR, fusion, explicit regularization, and learned priors across 2D, 2.5D, and 3D reconstruction.

Architectural diversity, imperfect observations, and urban-scale computation remain unresolved challenges. The practical research goal is increasingly automated reconstruction that preserves metric fidelity, valid topology, interpretable structure, and usability for digital twins.

The concluding outlook brings together generative models, multimodal semantic knowledge, CityGML-oriented interoperability, and dynamic updating. Anticipated gains in reasoning and generalization are research prospects; reliable reconstruction still depends on observations, appropriate priors, and explicit validation.
