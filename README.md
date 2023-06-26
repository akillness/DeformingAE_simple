# DeformingAE_simple
This is repository for studing about Deforming Autoencoding 
Deforming Autoencoder 의 구조를 이용해 필요로 하는 이미지의 shape을 분리해 내는 기술을 구현하고자 함


[![DAE Concept](/img/thumnail_DAE.PNG)](https://youtu.be/hwVGD6BYZd0)

# Deforming Autoencoder 의 개념
***
In this work we introduce Deforming Autoencoders, a generative model for images that disentangles shape from appearance in an unsupervised manner. 
As in the deformable template paradigm, shape is represented as a deformation between a canonical coordinate system (`template') and an observed image, while appearance is modeled in deformation-invariant, template coordinates. 
We introduce novel techniques that allow this approach to be deployed in the setting of autoencoders and show that this method can be used for unsupervised group-wise image alignment. 
We show experiments with expression morphing in humans, hands, and digits, face manipulation, such as shape and appearance interpolation, as well as unsupervised landmark localization. 
We also achieve a more powerful form of unsupervised disentangling in template coordinates, that successfully decomposes face images into shading and albedo, allowing us to further manipulate face images.

***
이 작업에서는 감독되지 않은 방식으로 모양과 모양을 분리하는 이미지 생성 모델인 Deforming Autoencoders를 소개합니다.
변형 가능한 템플릿 패러다임에서와 같이 모양은 표준 좌표계('템플릿')와 관찰된 이미지 사이의 변형으로 표현되는 반면 모양은 변형 불변 템플릿 좌표로 모델링됩니다.
우리는 이 접근 방식을 자동 인코더 설정에 배포할 수 있는 새로운 기술을 소개하고 이 방법이 비지도 그룹별 이미지 정렬에 사용될 수 있음을 보여줍니다.
인간, 손, 손가락의 표정 변형, 모양 및 모양 보간과 같은 얼굴 조작, 감독되지 않은 랜드마크 현지화에 대한 실험을 보여줍니다.
우리는 또한 얼굴 이미지를 음영 및 알베도로 성공적으로 분해하여 얼굴 이미지를 추가로 조작할 수 있도록 템플릿 좌표에서 더 강력한 형태의 감독되지 않은 얽힘 해제를 달성합니다.
