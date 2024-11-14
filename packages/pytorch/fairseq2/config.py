from jetson_containers import update_dependencies
from packaging.version import Version
from ..pytorch.version import PYTORCH_VERSION

def fairseq2(version, pytorch=None, requires=None):
    pkg = package.copy()
    
    pkg['name'] = f"fairseq2:{version.split('-')[0]}"  # remove any -rc* suffix
    
    if pytorch:
        pkg['depends'] = update_dependencies(pkg['depends'], f"pytorch:{pytorch}")
    else:
        pytorch = PYTORCH_VERSION
        
    if requires:
        pkg['requires'] = requires
        
    if not isinstance(pytorch, Version):
        pytorch = Version(pytorch)
        
    if len(version.split('.')) < 3:
        version = version + '.0'
        
    pkg['build_args'] = {
        'FAIRSEQ2_VERSION': version,
    }
    
    if pytorch == PYTORCH_VERSION:
        pkg['alias'] = 'fairseq2'
        
    return pkg

package = [
    # JetPack 5/6
    fairseq2('0.2.0', pytorch='2.1', requires='>=35.2,<=36.2'),

    # JetPack 5
    fairseq2('0.1.1', pytorch='1.13.1', requires='==35.*'),
]
