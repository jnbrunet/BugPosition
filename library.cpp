#include <sofa/core/ObjectFactory.h>
#include <sofa/core/objectmodel/BaseObject.h>
#include <sofa/core/objectmodel/Data.h>
#include <sofa/defaulttype/VecTypes.h>
#include <sofa/helper/accessor.h>

using sofa::core::RegisterObject;
using namespace sofa::core::objectmodel;
using namespace sofa::helper;

class TestComponent : public BaseObject {
public:
    SOFA_CLASS(TestComponent, BaseObject);
    using DataTypes = sofa::defaulttype::Vec3Types;
    using VecCoord = DataTypes::VecCoord;
    TestComponent() : d_position(initData(&d_position, "position", "Position vector")){}

    void init() override {
        Inherit1::init();
        auto positions = ReadAccessor<Data<VecCoord>>(d_position);
        test(positions.size());
    }
    void test(const sofa::Size & nb_of_nodes) {
        auto positions = ReadAccessor<Data<VecCoord>>(d_position);
        if (positions.size() != nb_of_nodes) {
            std::cout << "Just something to make sure the compiler compile this" << std::endl;
        }
    }
private:
    Data<VecCoord> d_position;
};

[[maybe_unused]]
static int c = RegisterObject("Test component")
        .add<TestComponent>();

extern "C" {
    void        initExternalModule() {}
    const char* getModuleName()    {return "BugPosition";}
    const char* getModuleVersion() {return "1.0";}
    const char* getModuleLicense() {return "LGPL";}
    const char* getModuleDescription() {return "Solving https://github.com/jnbrunet/caribou/issues/104";}
    const char* getModuleComponentList() {return "TestComponent";}
}