/**
 * @file test_ti_reg.cc
 */

#include <array>
#include <iostream>
#include <iomanip>
#include <cassert>

#include "gtest/gtest.h"

#include "ti_cc_regs.h"

using namespace testing;

class TestTiRegs : public Test
{
public:
    TestTiRegs() : Test()
    {
    }

};

TEST_F(TestTiRegs, dummy_test)
{
    EXPECT_TRUE(true);
}
